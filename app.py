from flask import Flask, render_template, request, redirect, session, flash, url_for
from models import db, User, GeneratedContent
from functools import wraps
from diffusers import DiffusionPipeline
from datetime import datetime
import threading
import time

app = Flask(__name__)
app.secret_key = 'alok@$uperman'

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# Global variables for the pipeline
pipe = None
pipeline_ready = False

# Function to load the pipeline in a background thread
def load_pipeline():
    global pipe, pipeline_ready
    try:
        print("Loading Stable Diffusion pipeline. This may take some time...")
        pipe = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
        pipe.load_lora_weights("Melonie/text_to_image_finetuned")
        pipe.to("cuda")  # Use GPU
        print("Pipeline loaded successfully.")
        pipeline_ready = True
    except Exception as e:
        print(f"Error loading pipeline: {e}")
        pipeline_ready = False

# Start loading the pipeline in a separate thread
pipeline_thread = threading.Thread(target=load_pipeline)
pipeline_thread.start()

# Middleware for authentication
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash('You need to log in to access this page.')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def home():
   
    # If not logged in, show the homepage with Login and Register options
    return render_template('home.html')
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists. Try a different one.', 'error')
        else:
            new_user = User(username=username)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['username'] = username
            flash('Logged in successfully!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.', 'error')
    
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    user = User.query.filter_by(username=session['username']).first()
    generated_contents = GeneratedContent.query.filter_by(user_id=user.id).order_by(GeneratedContent.generated_at.desc()).all()
    return render_template('dashboard.html', username=user.username, generated_contents=generated_contents)

@app.route('/generate-video', methods=['GET', 'POST'])
@login_required
def generate_video():
    global pipe, pipeline_ready
    image_url = None

    user = User.query.filter_by(username=session['username']).first()

    if request.method == 'POST':
        if not pipeline_ready:
            flash("The pipeline is still loading. Please try again later.", "error")
            return redirect(url_for('generate_video'))

        prompt = request.form['prompt']
        try:
            # Insert a record with status "Processing"
            generated_content = GeneratedContent(
                user_id=user.id,
                prompt=prompt,
                status="Processing"
            )
            db.session.add(generated_content)
            db.session.commit()

            # Generate the image
            result = pipe(prompt)
            image = result.images[0]

            # Save the image locally
            image_path = f"static/generated_image_{session['username']}_{datetime.utcnow().timestamp()}.png"
            image.save(image_path)

            # Update the database record
            generated_content.image_paths = image_path
            generated_content.status = "Completed"
            generated_content.generated_at = datetime.utcnow()
            db.session.commit()

            # Set the URL for displaying the image
            image_url = url_for('static', filename=image_path.split('/')[-1])

            flash('Image generated successfully!', 'success')
        except Exception as e:
            flash(f"Error generating image: {str(e)}", 'error')

    return render_template('generate-video.html', image_url=image_url)

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

# AI Video and Image Generation System Assignment  

Welcome to the **AI Video and Image Generation System Assignment**! This project is designed to assess your programming skills, creativity, problem-solving abilities, and ability to work with AI tools. Your task is to create a Python-based system that takes a user-provided text prompt, generates videos and images based on the text, and stores them for user access. The system should also notify the user when the generated content is ready.

---

## **Assignment Tasks**

### **Part 1: Text-to-Video and Text-to-Image Generation**
1. Accept a text prompt from the user.  
2. Generate at least:
   - **5 videos**: Use AI video generation tools like [RunwayML](https://runwayml.com/) or other accessible APIs.  
   - **5 images**: Use AI tools such as OpenAI’s DALL·E or Stable Diffusion.  
3. Save the generated content:
   - Videos should be saved as `.mp4` files.
   - Images should be saved as `.jpg` or `.png` files.
   - Store them in a directory named `generated_content/<user_id>/`.  

---

### **Part 2: Storing and Managing Content**
1. Maintain a database (SQL or any other DB) with the following structure:
   - `user_id` (unique identifier for the user)
   - `prompt` (text provided by the user)
   - `video_paths` (list of file paths to the generated videos)
   - `image_paths` (list of file paths to the generated images)
   - `status` (generation status: "Processing" or "Completed")
   - `generated_at` (timestamp of content generation)
2. Once the generation is complete:
   - Mark the status as **"Completed"** in the database.  
   - Notify the user that their content is ready (via email or console output) at specified time.  

---

### **Part 3: User Access and Web Page Display**
1. Create a simple **web page** using Flask or FastAPI or any other framework to display the content:  
   - The page should allow users to log in using a unique identifier (`user_id`).  
   - If the user has completed content, display:
     - Videos in a gallery view with playback functionality.
     - Images in a grid layout.  
2. If the content is still processing, show a message:  
   - _"Your content is being generated. Please check back later."_  
3. Log every user login attempt and content view in the database.

---

### **Part 4: Notifications**
1. Notify the user when their content is ready:
   - Use email or a system notification (e.g., desktop notification or in-terminal message).  
   - Include a link to the web page where they can view their content.  
2. Allow users to specify a "notification time" for when they'd like to receive the notification.  

---

## **Technical Requirements**
- **Programming Language**: Python or any language of your choice  
- **AI APIs**:
  - Video Generation: Use tools like [RunwayML](https://runwayml.com/) or [Pictory.ai](https://pictory.ai/) or any other tool.  
  - Image Generation: Use OpenAI’s DALL·E, [Stable Diffusion](https://stability.ai/), or other APIs.  
- **Framework**: Flask or FastAPI or any other of your choice for the web interface.  
- **Database**: SQL or any other database for storing user and generation data.  
- **File Storage**: Store generated content in a structured directory format.  

---

## **Setup Instructions**

### **Step 1: Clone the Repository**  
```bash
git clone <your-repository-url>
cd ai-generation-system
```

### **Step 2: Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **Step 3: Update Configuration**  
- Add your API keys for AI tools in `main.py`.  
- Update email credentials or notification configurations if required.

### **Step 4: Run the System**  
```bash
python main.py  # Starts the video and image generation service.
python web_app.py  # Starts the web server for user access.
```

---

## **Submission Guidelines**  

### **1. Code Repository**  
- Submit a GitHub repository containing your complete code, properly structured and testable.  
- Include a clear `README.md` file with setup instructions and usage details.  

### **2. Video Explanation**  
- Record a video (max 5 minutes) explaining:  
  - How to set up and run the project.  
  - A brief walkthrough of your code.  
  - A short introduction about yourself.  
- Upload the video to a platform (e.g., Internshalla or Google Drive) and share the link.  

---

## **Evaluation Process**  
Submissions will be evaluated based on:  
1. **Functionality**: Correct implementation of content generation, notification, and user access.  
2. **Code Quality**: Organized, readable, and efficient code.  
3. **Web Interface**: User-friendly and intuitive design.  
4. **Documentation**: Clear and detailed README.md and comments.  
5. **Presentation**: A professional and concise video explanation.  

---

## **Results**  
You will be notified within 24 hours if your assignment is shortlisted.  

---

**Good Luck!**  
We look forward to reviewing your submission. If you have any questions, don’t hesitate to reach out!  

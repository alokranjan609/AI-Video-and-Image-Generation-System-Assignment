from diffusers import DiffusionPipeline

# Load the base pipeline
pipe = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")

# Load LoRA weights
pipe.load_lora_weights("Melonie/text_to_image_finetuned")

# Define the prompt for image generation
prompt = "two dogs barking"

# Generate the image
image = pipe(prompt).images[0]

# Save the generated image
image.save("lora_generated_image1.png")

print("Image generation complete. Check 'lora_generated_image.png' in the current directory.")

from PIL import Image, ImageDraw, ImageFont
import time

def scale_and_overlay_text(img, font, output_path, scale_factor, text, font_size=80):
    # Start timing
    start_time = time.perf_counter()

    # Get the original size
    width, height = img.size
    
    # Calculate new size
    new_size = (int(width * scale_factor), int(height * scale_factor))
    
    # Resize the image
    img_resized = img.resize(new_size, Image.NEAREST)
    
    # Create a drawing object
    draw = ImageDraw.Draw(img_resized)

    # Calculate text position (centered)
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    position = ((new_size[0] - text_width) / 2, (new_size[1] - text_height) * 3 / 4)
    
    # Draw the text
    draw.text(position, text, font=font, fill=(255, 255, 255, 128))
    
    # Save the result
    img_resized.save(output_path)

    # End timing
    end_time = time.perf_counter()
    runtime_ms = (end_time - start_time) * 1000  # Convert to milliseconds
    print(f"Processing time: {runtime_ms:.2f} milliseconds")

# Usage
input_path = "input.jpg"
output_path = "output.jpg"
font_path = "/System/Library/Fonts/Helvetica.ttc"
font_size = 80
scale_factor = 1.1
text = "Hello, World!"

# Load image and font outside of the timed function
img = Image.open(input_path)
font = ImageFont.truetype(font_path, font_size)

scale_and_overlay_text(img, font, output_path, scale_factor, text, font_size)

# Close the image after processing
img.close()
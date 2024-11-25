from PIL import Image, ImageDraw, ImageFont
import os

def create_placeholder_image(filename, text, size=(300, 300)):
    image = Image.new('RGB', size, color='#f0f0f0')
    draw = ImageDraw.Draw(image)
    
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except IOError:
        font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    position = ((size[0]-text_width)/2, (size[1]-text_height)/2)
    draw.text(position, text, fill='#333333', font=font)

    if not os.path.exists('media/sample_images'):
        os.makedirs('media/sample_images')
    
    image.save(f'media/sample_images/{filename}')
    print(f"Created {filename}")

# Create placeholder images
products = ['Laptop', 'Smartphone', 'T-Shirt', 'Novel', 'Coffee Maker']
for product in products:
    create_placeholder_image(f"{product.lower().replace(' ', '-')}.jpg", product)

print("All placeholder images created successfully.")


import os
from PIL import Image

dir = r"C:\Users\gabri\Fish1"
allowed_formats = ['.png', '.jpeg', '.jpg', '.gif', '.avif']  # List of allowed file formats

for filename in os.listdir(dir):
    if not any(filename.endswith(ext) for ext in allowed_formats):
        continue  # Skip files with unsupported formats
    name, ext = os.path.splitext(os.path.basename(filename))
    image_path = os.path.join(dir, filename)
    # Open the image
    Bild = Image.open(image_path)
    # Convert and save as JPG
    if ext.lower() == '.gif':  # Convert GIF to JPG
        Bild.seek(0)  # Go to the first frame
        Bild = Bild.convert("RGB")  # Convert image to RGB mode (required for JPG)
    elif ext.lower() == '.avif':  # Convert AVIF to JPG
        Bild = Bild.convert("RGB")  # Convert image to RGB mode (required for JPG)
    Bild.save(os.path.join(dir, f"{name}.jpg"))

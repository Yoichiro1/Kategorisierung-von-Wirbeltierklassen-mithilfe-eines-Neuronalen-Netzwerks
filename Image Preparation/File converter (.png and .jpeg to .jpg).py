import os
from PIL import Image

dir = r"C:\Users\gabri\images\allimages"
erlaubte_formate = ['.png', '.jpeg', '.jpg', '.gif', '.avif', 'img', 'webp', 'tiff'] 

for filename in os.listdir(dir):
    if not any(filename.endswith(ext) for ext in erlaubte_formate):
        continue  
    name, ext = os.path.splitext(os.path.basename(filename))
    image_path = os.path.join(dir, filename)
    Bild = Image.open(image_path)
    if ext.lower() == '.gif': 
        Bild.seek(0)  
        Bild = Bild.convert("RGB")  
    elif ext.lower() == '.avif':  
        Bild = Bild.convert("RGB")  
    elif ext.lower() == '.jpeg':
        Bild = Bild.convert('RGB')
    elif ext.lower() == '.png':
        Bild = Bild.convert('RGB')
    elif ext.lower() == '.tiff':
        Bild = Bild.convert('RGB')
    elif ext.lower() == '.webp':
        Bild = Bild.convert('RGB')
    elif ext.lower() == '.img':
        Bild = Bild.convert('RGB')
    elif ext.lower() == ".jpg":
        continue
    Bild.save(os.path.join(dir, f"{name}.jpg"))
    os.remove(os.path.join(dir, os.path.basename(filename)))

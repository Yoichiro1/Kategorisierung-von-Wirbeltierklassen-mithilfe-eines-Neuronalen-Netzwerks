import os
from PIL import Image

dir = r"C:\Users\gabri\Fish1"
erlaubte_formate = ['.png', '.jpeg', '.jpg', '.gif', '.avif'] 

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
    Bild.save(os.path.join(dir, f"{name}.jpg"))

import os
from PIL import Image

dir = r"" # absoluter Pfad zum Ordner, worin die Bilder gespeichert sind.

erlaubte_formate = ['.png', '.jpeg', '.jpg', '.gif', '.avif', 'img', 'webp', 'tiff'] 

for filename in os.listdir(dir):
    # Überprüft, ob das Bild ein erlaubtes Format hat
    if not any(filename.endswith(ext) for ext in erlaubte_formate):
        os.remove(os.path.join(dir, os.path.basename(filename)))
        continue  
        
    name, ext = os.path.splitext(os.path.basename(filename))
    image_path = os.path.join(dir, filename)
    Bild = Image.open(image_path)
    
    # konvertiert das Bild ins RGB-Format, falls das Bild nicht eine ".jpg"-Datei ist, damit das Neuronale Netzwerk alle Bilder verwenden kann
    if ext.lower() == '.gif': 
        Bild.seek(0)  # Das Bild wird zum ersten Frame zurückgespult 
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
        
    Bild.save(os.path.join(dir, f"{name}.jpg")) # Das Bild wird als eine ".jpg"-Datei gespreichert
    os.remove(os.path.join(dir, os.path.basename(filename))) # Das ursprüngliche Bild wird gelöscht

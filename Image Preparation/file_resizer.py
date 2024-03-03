import os
import PIL
from PIL import Image

dir=r'' # absoluter Pfad zum Ordner, worin die Bilder gespeichert sind.
for file in os.listdir(dir):
    Bild=os.path.join(file, dir)
    img=Image.open(Bild) # Lädt das Bild
    img=img.resize((200,200)) # Verändert die Grösse/ Auflösung des Bildes. Grösse Angeben.
    img.save(Bild) # Speichert das Bild im gleichen Ordner.

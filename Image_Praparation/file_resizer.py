import os
import PIL
from PIL import Image
dir=r'C:\Users\username\directory'
for file in os.listdir(dir):
    Bild=dir+'/'+file
    img=Image.open(Bild)
    img=img.resize((200,200))
    img.save(Bild)

import keras
import os
import tkinter as tk
from tkinter import filedialog as fd #kopiert
import PIL
from PIL import Image
import cv2
import numpy as np
def nn_auswählen():
    model = keras.models.load_model(path + "\{file_name}.keras")

#kopiert
root = Tk()
root.withdraw()

image_given = False
def bild_auswählen:
    while image_given = False  
        folder_selected = fd.askopenfilename()
        folder_name = os.path.basename(folder_selected)
        if folder_name.find(".jpg" or ".jpeg" or ".png" or ".gif" or ".avif") != -1: #GPT
            image_given = True
        else:
            print("Error")
def reformat_image(): 
    name, ext = os.path.splitext(folder_name)
    image_path = os.path.join(dir, folder_name)
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
reformat_image()
img =Image.open(folder_selected)
img =image.resize((200,200))
img.save(folder_selected)


#zu np konvertieren
normalized_image=[]

image = cv2.imread(img)
image = image.astype(np.float32)
max_intensity = 255.0  # For 8-bit images
normalized_custom = image / max_intensity
normalized_image.append(normalized_custom)
np.array(normalized_image)
#Modell Anwenden
prediction = model.predict(input_data) #GPT
print(prediction)

import keras
import os
import tkinter as tk
from tkinter import filedialog as fd #kopiert
import PIL
from PIL import Image
import cv2
import numpy as np

path = os.getcwd()
file_name = input("Name deines Neuronalen Netzwerks: ")
model = keras.models.load_model(path + "\{file_name}.keras")

#kopiert
root = Tk()
root.withdraw()

image_given = False
while image_given = False  
    folder_selected = fd.askopenfilename()
    folder_name = os.path.basename(folder_selected)
    if folder_name.find(".jpg" or ".jpeg" or ".png") != -1: #GPT
        image_given = True
    else:
        print("Error")
def reformat_image():
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
reformat_image()
img =Image.open(folder_selected)
img =image.resize((200,200))
img.save(folder_selected)
 
#zu np konvertieren

prediction = model.predict(input_data) #GPT
print(prediction)

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

img =Image.open(folder_selected)
img =image.resize((200,200))
img.save(folder_selected)
 
#zu np konvertieren

prediction = model.predict(input_data) #GPT
print(prediction)

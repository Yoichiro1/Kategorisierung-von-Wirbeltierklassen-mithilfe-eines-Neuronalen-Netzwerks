import keras
import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd #kopiert
import PIL
from PIL import Image
import cv2
import numpy as np
def nn_auswählen():
    nn_given = False  
    nn_selected = fd.askopenfilename()
    nn_name = os.path.basename(folder_selected)
    if folder_name.find(".keras") != -1:
        nn_given = True            
    else:    
        r3 = Tk()
        w3 = Label(r3, text="Error. File is not an ".keras" file.")
        w3.pack()
        r3.mainloop()

def bild_auswählen():
    bild_given = False  
    folder_selected = fd.askopenfilename()
    folder_name = os.path.basename(folder_selected)
    exts = [".jpg", ".jpeg", ".png", ".gif", ".avif"]
    for ext in exts:
        if folder_name.find(ext) != -1:
           bild_given = True
           print("abc")            
    if bild_given == False:    
        r2 = Tk()
        w2 = Label(r2, text="Error. File is not an image file.")
        w2.pack()
        r2.mainloop()

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


def image_to_np():
    normalized_image=[]
    image = cv2.imread(img)
    image = image.astype(np.float32)
    max_intensity = 255.0  # For 8-bit images
    normalized_custom = image / max_intensity
    normalized_image.append(normalized_custom)
    input_data = np.array(normalized_image)

def predict():
    if bild_given and nn_given == True:
        reformat_image()
        image_to_np()
        prediction = model.predict(input_data) #GPT    
        r4 = Tk()
        w4 = Label(r4, text=prediction)
        w4.pack()
        r4.mainloop()
    else:
        r5 = Tk()
        w5 = Label(r5, text="Error. You have to upload image and neuronal network.")
        w5.pack()
        r5.mainloop()
        
r = tk.Tk()
r.geometry("200x200")
r.title('Neuronales Netzwerk')
button_image = tk.Button(r, text='Upload image', width=25, command=bild_auswählen)
button_nn = tk.Button(r, text='Upload your neuronal network', width=25, command=nn_auswählen)
button_predict = tk.Button(r, text='Predict', width=25, command=predict)
button_quit = tk.Button(r, text='Quit', width=25, command=r.destroy)
button_image.pack()
button_nn.pack()
button_predict.pack()
button_quit.pack()
r.mainloop()

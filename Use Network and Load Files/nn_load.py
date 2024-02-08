import keras
import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd #kopiert
import PIL
from PIL import Image
import cv2
import numpy as np
bild_given=False
nn_given = False
folder_name = ""
folder_selected = ""
ordnerpfad = ""
nn_selected = ""
def nn_auswählen():
    global nn_given
    global nn_selected
    nn_given = False  
    nn_selected = fd.askopenfilename()
    nn_name = os.path.basename(nn_selected)
    if nn_name.find(".keras") != -1:
        nn_given = True            
    else:    
        r3 = Tk()
        w3 = Label(r3, text="Error. File is not an keras file.")
        w3.pack()
        r3.mainloop()

def bild_auswählen():
    global bild_given
    global folder_name
    global folder_selected
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
    global folder_name
    global folder_selected
    global ordnerpfad
    Bild = Image.open(folder_selected)
    ordnerpfad = os.path.dirname(folder_selected)
    name, ext = os.path.splitext(folder_name)
    if ext.lower() == '.gif': 
        Bild.seek(0)  
        Bild = Bild.convert("RGB")  
    elif ext.lower() == '.avif':  
        Bild = Bild.convert("RGB")  
    elif ext.lower() == '.jpeg':
        Bild = Bild.convert('RGB')
    elif ext.lower() == '.png':
        Bild = Bild.convert('RGB')
    Bild.save(os.path.join(ordnerpfad, f"{name}.jpg"))
    img =Image.open(folder_selected)
    img =img.resize((200,200))
    img.save(folder_selected)

def predict():
    global bild_given, nn_given
    global ordnerpfad
    global nn_selected
    if bild_given and nn_given == True:
        reformat_image()
        train_ds = keras.utils.image_dataset_from_directory(
        directory=os.path.dirname(ordnerpfad), image_size=(200, 200) )
        model = keras.saving.load_model(nn_selected)
        prediction = model.predict(train_ds) #GPT    
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

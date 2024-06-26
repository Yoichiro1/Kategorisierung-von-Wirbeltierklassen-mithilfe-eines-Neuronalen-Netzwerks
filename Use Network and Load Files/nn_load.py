import keras
import tensorflow as tf
import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageTk
import numpy as np
import shutil

#Definieren von Variabeln

bild_given = False
nn_given = False
folder_name = ""
folder_selected = ""
ordnerpfad = ""
nn_selected = ""
copy_path = ""

# Funktion, um ein Neuronales Netzwerk auszuwählen
def nn_auswählen():
    global nn_given
    global nn_selected
    nn_given = False  
    nn_selected = fd.askopenfilename()
    nn_name = os.path.basename(nn_selected)
    if nn_name.endswith(".keras"):
        nn_given = True
        nn_label.config(text="Selected Neural Network: " + nn_name)  # Update the label with the selected neural network name
    else:    
        r3 = Tk()
        w3 = Label(r3, text="Error. File is not a .keras file.")
        w3.pack()
        r3.mainloop()

# Funktion, um ein Bild auszuwählen
def bild_auswählen():
    global bild_given
    global folder_name
    global folder_selected
    global prediction_label
    bild_given = False  
    folder_selected = fd.askopenfilename()
    folder_name = os.path.basename(folder_selected)
    exts = [".jpg", ".jpeg", ".png", ".gif", ".avif"]
    # Überprüft, ob die ausgewählte Datei verwendbar ist.
    for ext in exts:
        if folder_name.endswith(ext):
            bild_given = True
            break
    if not bild_given:    
        r2 = Tk()
        w2 = Label(r2, text="Error. File is not an image file.")
        w2.pack()
        r2.mainloop()
    else:
        # Zeigt eine Bildvorschau.
        display_image()
        prediction_label.config(text="")  # Löscht die vorherige Vorhersage, wenn ein neues Bild ausgewählt wurde

def display_image():
    global folder_selected
    global label_preview
    image = Image.open(folder_selected)
    image.thumbnail((50, 50))  # Verändert die Grösse des Eingabe-Bildes
    photo = ImageTk.PhotoImage(image)
    label_preview.config(image=photo)
    label_preview.image = photo  # Keep a reference to the image to prevent garbage collection

# Wandelt das ausgewählte Bild zu einem ".jpg"-Datei um.
def reformat_image(): 
    global folder_name
    global folder_selected
    global ordnerpfad
    global image
    global copy_path
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
    
    # Schafft eine Kopie des Originales Bilds
    copy_path = os.path.join(ordnerpfad, f"{name}_copy{ext}")
    shutil.copyfile(folder_selected, copy_path)

    #Konfiguriert die Grösse der Kopie des Bilds
    img = Image.open(copy_path)
    img = img.resize((50,50))
    img.save(copy_path)
    image = np.array(img, dtype=np.float32) / 255.0
    image = np.expand_dims(image, axis=0)
    print(image)

def predict():
    #Funktion, die das Netzwerk wirklich verwendet
    global bild_given, nn_given
    global ordnerpfad
    global nn_selected
    global prediction_label
    if bild_given and nn_given == True:
        reformat_image()
        model = keras.models.load_model(nn_selected)
        prediction = model.predict(image) #GPT 
        prediction = prediction.tolist()
        prediction2 = []
        for liste_prediction in prediction:
            for element_liste_prediction in liste_prediction:
                prediction2.append(element_liste_prediction)
        prediction_a = prediction2[0]
        prediction_f = prediction2[1]
        prediction_r = prediction2[2]
        prediction_s = prediction2[3]
        prediction_v = prediction2[4]
        prediction = [prediction_a, prediction_f, prediction_r, prediction_s, prediction_v]
        prediction = max(prediction)
        if prediction == prediction_a:
            prediction_tier = "Amphibie"
        elif prediction == prediction_f:
            prediction_tier = "Fisch"
        elif prediction == prediction_r:
            prediction_tier = "Reptil"
        elif prediction == prediction_s:
            prediction_tier = "Säugetier"
        elif prediction == prediction_v:
            prediction_tier = "Vogel"
        
        # Zeigt das Output des Netzwerk unter dem Bild
        prediction_label.config(text="Prediction: " + prediction_tier, fg= 'white')
    else:
        r5 = Tk()
        w5 = Label(r5, text="Error. You have to upload image and Neural Network.")
        w5.pack()
        r5.mainloop()

    # Löscht die Kopie nach dessen Verwendung
    if os.path.exists(copy_path):
        os.remove(copy_path)
    else:
        print("The file does not exist")

        
r = tk.Tk()
r.geometry("1080x1920")
r.title('Neuronales Netzwerk')
r.configure(bg='#282927')  # Setzt Hintergrundfarbe

# Neural Network Label
nn_label = Label(r, text="", bg='#282927', fg='white', font= (None, 16))
nn_label.pack()

# Ladet und Zeigt eine Vorschau des Bildes
label_preview = Label(r)
label_preview.pack()

# Zeigt die Vorhersage des Netzwerks
prediction_label = Label(r, text="", bg= '#282927', font= (None, 16))
prediction_label.pack()

# Buttons
button_image = tk.Button(r, text='Upload image', width=25, command=bild_auswählen, bg= '#303633' , fg='white') #Schafft den Knopf für das Auswählen eines Bilds
button_nn = tk.Button(r, text='Upload your Neural Network', width=25, command=nn_auswählen, bg= '#303633' , fg='white')#Schafft den Knopf für das Auswählen Netzwerks
button_predict = tk.Button(r, text='Predict', width=25, command=predict, bg= '#303633' , fg='white')#Schafft den Knopf für das Benutzen des Netzwerks
button_quit = tk.Button(r, text='Quit', width=25, command=r.destroy, bg= '#303633' , fg='white')#Schafft den Knopf für das Beenden des Programms

#Fertiges ausführen der Button-Commands
button_image.pack()
button_nn.pack()
button_predict.pack()
button_quit.pack()

r.mainloop()

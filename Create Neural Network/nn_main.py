# Alle Module importieren
import numpy as np
import cv2
import keras
import tensorflow as tf
from keras.models import Sequential as sq
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras import layers 
from keras import models
import os
import matplotlib.pyplot as plt


# Den absoluten Pfad des Ordners für Trainings- und Testbilder einsetzen
train_dir = r""
test_dir = r""

# Anzahl Epochen des Trainingsverfahren (In jeder Epoche werden alle Daten dem Netzwerk gefüttert.)
num_epochs = 20


# Bilder laden
train_ds = keras.utils.image_dataset_from_directory(
    directory=train_dir, # Pfad zum Ordner
    labels='inferred', # Definiert Label der Daten nach der Struktur des Ordners
    label_mode='categorical', # Definiert den Modus der Label: kategorisch
    batch_size=200, # Definiert die Grösse eines Batches
    image_size=(50, 50)) # Grösse der vom Netzwerk verarbeiteten Bilder 
validation_ds = keras.utils.image_dataset_from_directory(
    directory=test_dir,
    labels='inferred',
    label_mode='categorical',
    batch_size=50,
    image_size=(50, 50))


# Bilder vorbereiten
def preprocess_image(image, label):
    image = tf.cast(image, tf.float32) # Wandelt die Daten der Bilder in den Datentyp "float32" um (Pixelwerte im Bereich 0-255) GPT
    image = image / 255.0 # Dividiert die Pixelwerte durch 255, damit sie im Bereich von 0-1 sind. Dient der Stabiliät des Netzwerks.
    return image, label

# Anwendung der Funktion auf die Trainings- und Testbilder
train_ds = train_ds.map(preprocess_image)
validation_ds = validation_ds.map(preprocess_image)


# Das Neuronale Netzwerk aufbauen
def apply_Model():
    model = keras.Sequential([ # Modell definieren durch "Sequential"(gruppiert mehrere Schichten)    
        layers.Conv2D(32, kernel_size=(3, 3), activation="relu", input_shape = (50, 50, 3)), # Eine Convolutional-Schicht mit 32 3x3 Filter, mit der Aktivierungsfunktion "ReLu" und mit einer Eingabeform des Bildes von 50x50x3 (RGB).
        layers.BatchNormalization(), # Eine BatchNormalization-Schicht, die die Aktivierungswerte eines neuronalen Netzwerks normalisieren.
        layers.MaxPooling2D(pool_size=(2, 2)), # Eine MaxPooling-Schicht, die nur den maximalen Wert für jedes 2x2 Feld im Bild weitergibt.
        layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
        layers.BatchNormalization(),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(128, kernel_size=(3, 3), activation="relu"),
        layers.BatchNormalization(),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(), # Wandelt das 2-dimensionale Feld zu einem 1-dimensionalen Array
        layers.Dense(2304, activation = "relu"), # Eine vollständig verbundene Dense-Schicht mit 2304 Neuronen und mit der Aktivierungsfunktion "ReLu"
        layers.Dropout(0.2), # Dropout-Layer (setzt mit einer Wahrscheinlichkeit von 0.2 den Wert eines Neurons der vorherigen Schicht auf 0, verhindert Overfitting) 
        layers.Dense(512, activation = "relu"),
        layers.Dropout(0.2),
        layers.Dense(128, activation = "relu"),
        layers.Dropout(0.2),
        layers.Dense(64, activation = "relu"),
        layers.Dropout(0.2),
        layers.Dense(5, activation="softmax"), # Output-Layer mit 5 Neuronen für 5 Klassen und mit der Aktivierungsfunktion "softmax"
    ])
    # Modell für das Training konfigurieren
    global history
    history = model.compile(optimizer= keras.optimizers.Adam(learning_rate = 0.001), # Definiert den Optimierer des Modells als "adam" (eine stochastische Gradientenabstiegsmethode, die auf der adaptiven Schätzung von Momenten erster und zweiter Ordnung basiert) mit Learning-Rate von 0.001
                  loss='categorical_crossentropy', # Definiert Loss-Funktion als "categorical_crossentropy": Gibt an, wie weit die Vorhersage des Modells von den richtigen Werten entfernt sind.
                  metrics=['accuracy']) # Definiert die Metrik (beurteil das Modell) als "accuracy" (gibt die Genauigkeit in Dezimaldarstellung an)
    
    # Modell trainieren
    model.fit(train_ds, epochs=num_epochs, validation_data = validation_ds) # Trainingsverfahren des Modells, nach jeder Epoche wird das Modell mit den Testdaten getestet

    # Modell speichern
    filename_given = False
    path = os.getcwd()
    while not filename_given:
        filename = input("Name der Datei:")
        if not os.path.exists(os.path.join(path, f"{filename}.keras")):
            filename_given = True
        else:
            print("Error, file already exists.")
    model.save(os.path.join(path, f"{filename}.keras"))
  
apply_Model()

# Kopiert
# Lernverlauf des Modells für Trainings- und Testdaten anzeigen lassen
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.xticks(range(1, num_epochs + 1)) # GPT
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.xticks(range(1, num_epochs + 1)) # GPT
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()


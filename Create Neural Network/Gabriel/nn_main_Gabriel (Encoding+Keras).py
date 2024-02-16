import numpy as np
import cv2
import random as rd
from keras.models import Sequential as Sq
from keras.layers import Dense as Ds
from keras.layers import Conv2D, MaxPooling2D, Flatten
from keras.utils import to_categorical
from keras import layers 
from keras import models
import os
#REPLACE DIR VARIABLES


dir = r'C:\Users\gabri\images\allimages'

normalized_images_path = os.path.join(dir, 'Normalized_Images.npy')
labels_path = os.path.join(dir, 'Labels.npy')
test_data_path = os.path.join(dir, 'Testdaten.npy')
test_labels_path = os.path.join(dir, 'Test_Labels.npy')

Normalisierte_Bilder = np.load(normalized_images_path)
Labels = np.load(labels_path)
Testdaten = np.load(test_data_path)
Test_Labels = np.load(test_labels_path)


# Index Labels GPT 
label_to_index = {label: index for index, label in enumerate(np.unique(Labels))}
index_to_label = {index: label for label, index in label_to_index.items()}

#Create an array of indexed Labels
Labels_encoded = np.array([label_to_index[label] for label in Labels])
Test_Labels_encoded = np.array([label_to_index[label] for label in Test_Labels])

#Encode Labels GPT
Labels = to_categorical(Labels_encoded)
Test_Labels = to_categorical(Test_Labels_encoded)

#Reshaping the numpy arrays so they can fit the Network
Normalisierte_Bilder = Normalisierte_Bilder.reshape(-1, 200, 200, 3)
Testdaten= Testdaten.reshape(-1, 200, 200, 3)

#CONSTRUCTING MODEL 
def apply_Model():
    model = models.Sequential([
        layers.Flatten(input_shape=(200, 200, 3)),
        layers.Dense(2048, activation='relu'),     
        layers.Dense(1024, activation='relu'),  
        layers.Dense(1024, activation='relu'),     
        layers.Dense(512, activation='relu'),
        layers.Dense(512, activation='relu'),
        layers.Dense(256, activation='relu'),
        layers.Dense(256, activation='relu'),
        layers.Dense(128, activation='relu'), 
        layers.Dense(128, activation='relu'),     
        layers.Dense(64, activation='relu'),
        layers.Dense(len(label_to_index), activation='softmax')  
    ])
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',  
                  metrics=['accuracy'])

    #APPLYING NPY ARRAYS TO MODEL
    model.fit(Normalisierte_Bilder, Labels, epochs=10, batch_size=250)
    model.evaluate(Testdaten, Test_Labels, batch_size=50)

    #NAMING AND SAVING THE NN
    filename_given = False
    path = os.getcwd()
    while not filename_given:
        filename = input("Name der Datei:")
        if os.path.exists(os.path.join(path, f"{filename}.keras")):
            filename_given = True
            print("Error, file already exists.")
        else:
         model.save(os.path.join(path, f"{filename}.keras"))

apply_Model()

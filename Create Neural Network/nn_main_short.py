import numpy as np
import cv2
import random as rd
import math as m
import keras
import tensorflow as tf
from keras.models import Sequential as sq
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras import layers 
from keras import models
import os
import pandas
#DISCLAIMER:For future me, Yo or anyone else who actually might be good at coding, I'm sorry.

#BEFORE: REPLACE AMOUNT OF IMAGES, DIR NAME AND MAKE ALL IMAGES .JPG FILES
train_dir = r"C:\Users\gabri\PA Dataset\ds_train_images_3x augmentation"
test_dir = r"C:\Users\gabri\PA Dataset\allimages"

train_ds = keras.utils.image_dataset_from_directory(
    directory=train_dir,
    labels='inferred',
    label_mode='categorical',
    batch_size=20,
    image_size=(200, 200))
validation_ds = keras.utils.image_dataset_from_directory(
    directory=test_dir,
    labels='inferred',
    label_mode='categorical',
    batch_size=10,
    image_size=(200, 200))
def preprocess_image(image, label):
    image = tf.cast(image, tf.float32)
    image = image / 255.0 # GPT
    return image, label

# Anwendung der Skalierungsfunktion auf die Trainings- und Validierungsdaten
train_ds = train_ds.map(preprocess_image)
validation_ds = validation_ds.map(preprocess_image)
#CONSTRUCTING MODEL
def apply_Model():
    model = keras.Sequential(
        [
            layers.Conv2D(64, kernel_size=(3, 3), activation="relu", input_shape = (200, 200, 3)),
            layers.BatchNormalization(),
            layers.MaxPooling2D(pool_size=(2, 2)),
            layers.Conv2D(128, kernel_size=(3, 3), activation="relu"),
            layers.BatchNormalization(),
            layers.MaxPooling2D(pool_size=(2, 2)),
            layers.Conv2D(256, kernel_size=(3, 3), activation="relu"),
            layers.BatchNormalization(),
            layers.MaxPooling2D(pool_size=(2, 2)),
            layers.Conv2D(512, kernel_size=(3, 3), activation="relu"),
            layers.BatchNormalization(),
            layers.MaxPooling2D(pool_size=(2, 2)),
            layers.Flatten(),
            layers.Dense(512, activation = "relu"),
            layers.Dropout(0.3),
            layers.Dense(256, activation = "relu"),
            layers.Dropout(0.3),
            layers.Dense(128, activation = "relu"),
            layers.Dropout(0.2),
            layers.Dense(128, activation = "relu"),
            layers.Dropout(0.2),
            layers.Dense(64, activation = "relu"),
            layers.Dropout(0.2),
            layers.Dense(64, activation = "relu"),
            layers.Dropout(0.2),
            layers.Dense(5, activation="softmax"),
        ]
    )

    model.compile(optimizer= keras.optimizers.Adam(learning_rate = 0.001),
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    model.summary()
    model.fit(train_ds, epochs=20, validation_data = validation_ds)
    model.evaluate(validation_ds)

    # NAMING AND SAVING THE NN
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
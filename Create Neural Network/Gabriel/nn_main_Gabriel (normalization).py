import numpy as np
import cv2
import os
#REPLACE DIR VARIABLES
train_dir = r"C:\Users\gabri\images\allimages"
test_dir = r"C:\Users\gabri\images\alltestimages"

#Images need to be Normalized so they fit the parameters necessary to use the keras.models feature later down the line.
#The directory is a flexible parameter as to make the code more readable and condensed

def normalize_images(directory):
    normalized_images = []
    labels = []
    for filename in os.listdir(directory):
        if filename.endswith('.jpg'):
            filepath = os.path.join(directory, filename)
            image = cv2.imread(filepath)
            if image is not None:
                # Normalize pixel values to the range [0, 1]
                normalized_image = image.astype(np.float32) / 255.0
                normalized_images.append(normalized_image)
                # Extract class label from filename
                label = filename.split('_')[0]  # Assuming label is before the first underscore GPT
                labels.append(label)

    # Convert lists to NumPy arrays
    normalized_images = np.array(normalized_images)
    labels = np.array(labels)
    return normalized_images, labels

def preprocess_training_data(train_dir):
    # Normalize training images and create labels
    train_images, train_labels = normalize_images(train_dir)
    #Deciding the names and location for saving the numpy arrays 
    np.save(os.path.join(train_dir, 'Normalized_Images.npy'), train_images)
    np.save(os.path.join(train_dir, 'Labels.npy'), train_labels)
    #print statements to make bugs/edge cases easier to spot and simplify debugging processes
    print('Training data processed.')

def preprocess_test_data(test_dir):
    # Normalize test images and create labels
    test_images, test_labels = normalize_images(test_dir)
    np.save(os.path.join(train_dir, 'Testdaten.npy'), test_images)
    np.save(os.path.join(train_dir, 'Test_Labels.npy'), test_labels)
    print('Test data processed.')


def preprocess_data(train_dir, test_dir):
    #calling both functions in one to make calling it easier
    preprocess_training_data(train_dir)
    preprocess_test_data(test_dir)
    

preprocess_data(train_dir, test_dir)

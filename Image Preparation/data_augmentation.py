import os
import cv2
import numpy as np
import random as rd

input_directory = r'C:\Users\aokik\pyworks\testest' # Den absoluten Pfad zum Ordner angeben.

# Data augmentieren
def augment_images_in_directory(input_dir):
    
    dir = ["amphibie", "fisch", "reptil", "saugetier", "vogel"]  # Liste der Ordner, worin sich die Bilder befinden.
    augmentation_list = ["rotate", "flip"] # Liste der Augmentationarten

    for directory in os.listdir(input_dir):
        if os.path.basename(directory) in dir:
            dir_path = os.path.join(input_dir, directory)
            for filename in os.listdir(dir_path):
                file_path = os.path.join(dir_path, filename)
                if os.path.isfile(file_path) and filename.lower().endswith('.jpg'):
            
                    image = cv2.imread(file_path) # Bild lesen
                    
                    
                    if image is not None: # Kontrollieren, ob die Bilder valid sind.
            
                        random_angles = np.random.randint(-45, 46, size=4) # Generiert 4 zufällige Rotationswinkel innerhalb von 45 Grad. GPT
                        rotation_angles = [45, 90, 180, 270] + list(random_angles) # Fügt zur Liste der zufälligen Winkel die Winkel 45, 90, 180, 270 zu.
                        augmentation = rd.choice(augmentation_list) # Wählt zufällig einen Winkel aus der Liste
                        
                        if augmentation == "rotate":
                            # rotieren, GPT
                            angle = rd.choice(rotation_angles)
                            rows, cols, _ = image.shape
                            rotation_matrix = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
                            rotated_image = cv2.warpAffine(image, rotation_matrix, (cols, rows))

                            # speichern
                            output_filename = os.path.splitext(filename)[0] + '_rotate_' + str(angle) + '.jpg'
                            output_path = os.path.join(dir_path, output_filename)
                            cv2.imwrite(output_path, rotated_image) # GPT

                            # spiegeln
                            flipped_image = cv2.flip(rotated_image, 1) # GPT

                            # speichern
                            output_filename = os.path.splitext(filename)[0] + '_rotate_flip.jpg'
                            output_path = os.path.join(dir_path, output_filename)
                            cv2.imwrite(output_path, flipped_image) # GPT
                        else:
                            # spiegeln
                            flipped_image = cv2.flip(image, 1) # GPT

                            # speichern
                            output_filename = os.path.splitext(filename)[0] + '_flip.jpg'
                            output_path = os.path.join(dir_path, output_filename)
                            cv2.imwrite(output_path, flipped_image) # GPT

                            # rotieren, GPT
                            angle = rd.choice(rotation_angles)
                            rows, cols, _ = flipped_image.shape
                            rotation_matrix = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
                            rotated_image = cv2.warpAffine(flipped_image, rotation_matrix, (cols, rows))

                            # speichern
                            output_filename = os.path.splitext(filename)[0] + '_flip_rotate_' + str(angle) + '.jpg'
                            output_path = os.path.join(dir_path, output_filename)
                            cv2.imwrite(output_path, rotated_image) # GPT
                    else:
                        print(f"Error: Could not read image file '{file_path}'")

augment_images_in_directory(input_directory)

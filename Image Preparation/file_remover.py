import os
import random

pfad = r"" # absoluter Pfad zum Ordner

# Löscht jedes Bild mit einer Wahrscheinlichkeit von 50%
for element in os.listdir(os.path.join(pfad)):
    x = random.randint(1, 101)
    if x < 50:
        os.remove(os.path.join(pfad, element))

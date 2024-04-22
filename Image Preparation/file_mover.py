import os
import shutil
import random

# absoluten Pfad zum Ordner, worin die Bilder sind, und zum Ziel-Ordner, wohin die Bilder verschoben werden sollen, angeben.
ordner_pfad = r""
ziel_ordner_pfad = r""

Auslesen = False # Einstellen, ob nur ein Teil (zufällig ausgewählt) der Bilder verschoben werden soll.
ordner_in_anderer_ordner = True # Einstellen, ob im oben angegebenen Ordner sich zusätzliche Ordner befinden, worin die Bilder gespeichert sind.

number = 1

def ordener_verschieben(ordner_pfad):
    global ziel_ordner_pfad, Auslesen, number
    
    for datei in os.listdir(ordner_pfad):
        if Auslesen == True:
            x = random.randint(1, 100) # Wählt eine zufällige Zahl zwischen 1 und 100 aus.
        else:
            x = 1
        if x <= 50: # Eine natürliche Zahl angeben. Diese Zahl entspricht dem Prozentsatz, dass ein Bild verschoben wird.
            datei_pfad = os.path.join(ordner_pfad, datei)
            neuer_dateiname = f"_{number}.jpg" # Einen beliebigen Dateinamen angeben. (Beachten, dass die Dateinamen schon vorhanden sind.)
            ziel_datei_pfad = os.path.join(ziel_ordner_pfad, neuer_dateiname)
            shutil.move(datei_pfad, ziel_datei_pfad) # Verschiebt die Datei zum Zielordner.
            number += 1
# Führt die Funktion oben, je nach Zustand der Variable "ordner_in_anderer_ordner" aus.
if ordner_in_anderer_ordner == True:
    for u_ordner in os.listdir(ordner_pfad):
        neuer_ordner_pfad = os.path.join(ordner_pfad, u_ordner)
        ordener_verschieben(neuer_ordner_pfad)
else:
    ordener_verschieben(ordner_pfad)

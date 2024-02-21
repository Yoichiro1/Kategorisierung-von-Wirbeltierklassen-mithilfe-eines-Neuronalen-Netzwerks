import os
import shutil
import random

ordner_pfad = r""
ziel_ordner_pfad = r""

Auslesen = False
ziel_ordner_in_anderer_ordner = True
number = 1

def ordener_verschieben(ordner_pfad):
    global ziel_ordner_pfad, Auslesen, number
    for datei in os.listdir(ordner_pfad):
        if Auslesen == True:
            x = random.randint(1, 101)
        else:
            x = 1
        if x < 51:
            datei_pfad = os.path.join(ordner_pfad, datei)
            neuer_dateiname = f"common_newt2_{number}.jpg"
            ziel_datei_pfad = os.path.join(ziel_ordner_pfad, neuer_dateiname)
            shutil.move(datei_pfad, ziel_datei_pfad)
            number += 1

if ziel_ordner_in_anderer_ordner == True:
    for u_ordner in os.listdir(ordner_pfad):
        neuer_ordner_pfad = os.path.join(ordner_pfad, u_ordner)
        ordener_verschieben(neuer_ordner_pfad)
else:
    ordener_verschieben(ordner_pfad)

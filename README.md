# Vorwort
Die folgende READMDE wurde nur für Benutzer von Windows 10/11 verfasst, die Programme wurden nur mit Python 3.11/3.12 getestet. 

Clarify Licensing and Legal



# Vorbereitung:
## Die Anaconda Distribution herunterladen 
(https://www.anaconda.com/download)
   ![Anaconda_Logo_RGB_Corporate](https://github.com/Yoichiro1/Neuronales-Netzwerk/assets/158302206/a3ec9da3-e883-493f-9fbf-dfd9866e5af5)

### Den Anaconda Installer starten


![Screenshot (3)](https://github.com/Yoichiro1/Neuronales-Netzwerk/assets/158302206/60558f8e-0d72-43f4-a420-51300d460938)

Hier "Next" clicken.



![Screenshot (4)](https://github.com/Yoichiro1/Neuronales-Netzwerk/assets/158302206/6c9a5c54-379b-4755-9357-e28a2fddc537)

Stimmen sie den AGBs zu.



![Screenshot (5)](https://github.com/Yoichiro1/Neuronales-Netzwerk/assets/158302206/7cf7f7c2-fcc3-4c4a-b7be-b50857d9212d)

Installieren sie nur für sich selbst Anaconda.




![Screenshot (6)](https://github.com/Yoichiro1/Neuronales-Netzwerk/assets/158302206/50bb9cca-d802-4ccb-8803-29836e98ceef)

Konfigurieren sie den Ort, an welchem sie das Programm haben wollen. (nach erstem stratup müssen sie es nicht mehr starten)


![Screenshot (7)](https://github.com/Yoichiro1/Neuronales-Netzwerk/assets/158302206/0f588711-36b8-42f1-9349-d5006df90a2b)

Mir empfehlen ihnen, diese Einstellungen auszuwählen.




## Die Neuste Python Version herunterladen (https://www.python.org/downloads/)

![Screenshot (9)](https://github.com/Yoichiro1/Neuronales-Netzwerk/assets/158302206/b7b3ab92-65c8-4e74-9826-4d89fdf0f4c4)


## Importieren sie die benötigte Installs in ihr Path Environment
 
### PIP Installs:

Um Zeit zu sparen, einfach: 

```
pip install -r requirements.txt
```
in powershell kopieren

![PA PIP Install Screeenshot - Copy](https://github.com/Yoichiro1/Neuronales-Netzwerk/assets/158302206/370cf232-31ef-4bd1-862b-1585f80c360a)

1.  pip install cv2 (old nn_main)
2.  pip install tk
3.  pip install tensorflow
4.  pip install keras
5.  pip install PIL (old nn_main)
6.  pip install numpy
7.  pip install bing_image_downloader (web scraper)
8.  pip install shutil
9.  pip install matplotlib


## Laden sie das Dataset herunter ()
   HIER SCREENSHOT EINFÜGEN
## Change the Directory (dir) variables (Code Containing such variables will have a comment just under all the library imports)
SCREEMSHOT MIT PFEIL HIER EINFÜGEN




# Vorgehen:
## Selbst ein Netzwerk Trainieren

### Ein Dataset selbst erschaffen

Der folgende Code kann zum automatisieren der Bildersuche verwendet werden:

````
import bing_image_downloader
from bing_image_downloader import downloader

dir= r'' # absoluter Pfad, wo die Bilder gespeichert werden soll.

downloader.download ("Suchbegriff", limit=300, output_dir= dir) # Lädt maximal 300 Bilder von "Suchbegriff" im oben festgelegten Ordner herunter.

````



### Dataset in den Code Importieren
![Screenshot 2024-04-21 184050](https://github.com/Yoichiro1/Kategorisierung-von-Wirbeltierklassen-mithilfe-von-Neuronalen-Netzwerken/assets/158302206/e6e89258-9ccb-442b-810f-28dac97987e3)

Hier "test_dir" und "train_dir" als Weg zur directory definieren.

### Den Code für nn_main_short gemäss ihren Ressourcen und Wünschen konfigurieren

Hier können sie die Anzahl Schichten oder Neuronen konnfigurieren

### Das fertige Modell als Datei speichern

Den Dateinamen am Ende hineinschreiben und die Datei wird mit diesem Namen gespeichert.

## Das Netwerk anwenden

### Ein Modell herunterladen

Wenn sie nicht selbst ein Modell haben, können sie hier eines unserer vortrainierten Modelle herunterladen. ()

### Den Code für nn_load starten

Konfigurieren sie die Bildergrössen-Variable auf die des Netzwerks. Diese steht bei unserem Netzwerk im Dateinamen, oder auf einer beigefügten .txt File.




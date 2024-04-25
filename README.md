# Vorwort
Die folgende READMDE wurde nur für Benutzer von Windows 10/11 verfasst, die Programme wurden nur mit Python 3.11/3.12 getestet. 





# Vorbereitung:

## Einen Code Editor Herunterladen

![VS CODE LOGO](https://github.com/Yoichiro1/Kategorisierung-von-Wirbeltierklassen-mithilfe-eines-Neuronalen-Netzwerks/assets/158302206/1c3aec83-af8f-4d27-bf5a-8c78efe5ba75)

Wir empfehlen VS Code, welches im Microsoft Store heruntergeladen werden kann.

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


## Laden sie ein Dataset herunter oder erstellen sie ihr eigenes
   ![Screenshot 2024-04-24 214435](https://github.com/Yoichiro1/Kategorisierung-von-Wirbeltierklassen-mithilfe-eines-Neuronalen-Netzwerks/assets/158302206/9dc3b65e-eff3-4f02-abec-70be09feaf87)




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

![image](https://github.com/Yoichiro1/Kategorisierung-von-Wirbeltierklassen-mithilfe-eines-Neuronalen-Netzwerks/assets/158302206/4a3be24e-0377-4be3-8733-ec2fc6265b0b)

Hier können sie die Anzahl Schichten oder Neuronen konfigurieren

### Das fertige Modell als Datei speichern

![Screenshot 2024-04-21 195851](https://github.com/Yoichiro1/Kategorisierung-von-Wirbeltierklassen-mithilfe-von-Neuronalen-Netzwerken/assets/158302206/14b81dc6-fed1-4925-909a-70ba6cab0e4c)

Den Dateinamen am Ende hineinschreiben und die Datei wird mit diesem Namen gespeichert.

## Das Netwerk anwenden

### Ein Modell herunterladen

![Screenshot 2024-04-24 214435](https://github.com/Yoichiro1/Kategorisierung-von-Wirbeltierklassen-mithilfe-eines-Neuronalen-Netzwerks/assets/158302206/760d2744-05b4-4559-97ba-91a6c3e8e24f)


Wenn sie nicht selbst ein Modell haben, können sie hier eines unserer vortrainierten Modelle herunterladen. (https://www.kaggle.com/datasets/yoichiro1/kategorisierung-von-wirbeltierklassen)



### Den Code für nn_load starten

![Screenshot 2024-04-14 182032](https://github.com/Yoichiro1/Kategorisierung-von-Wirbeltierklassen-mithilfe-eines-Neuronalen-Netzwerks/assets/158302206/d15da370-5b7f-4181-be59-740bafe6b153)

Konfigurieren sie die Bildergrössen-Variable auf die des Netzwerks. Diese steht bei unserem Netzwerk im Dateinamen, oder auf einer beigefügten .txt File.




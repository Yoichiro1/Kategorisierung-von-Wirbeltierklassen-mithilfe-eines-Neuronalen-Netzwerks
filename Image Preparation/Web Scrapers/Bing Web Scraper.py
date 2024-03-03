import bing_image_downloader
from bing_image_downloader import downloader

dir= r'' # absoluter Pfad, wo die Bilder gespeichert werden soll.

downloader.download ("", limit=300, output_dir= dir) # Lädt maximal 300 Bilder von "Suchbegriff" im oben festgelegten Ordner herunter.

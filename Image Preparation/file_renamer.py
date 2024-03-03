import os

dir = r"" # absoluter Pfad zum Ordner, worin die Bilder gespeichert sind.

for count, f in enumerate(os.listdir(dir)):
    f_name, f_ext = os.path.splitext(f)
    f_name = "_" + str(count+1) # Einen beliebigen Dateinamen angeben. (Beachten, dass die Dateinamen schon vorhanden sind.)
    new_name = f'{f_name}{f_ext}'
    os.rename(f, new_name) # Benennt die Datei um.

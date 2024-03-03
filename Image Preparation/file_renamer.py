import os

dir = r"" # absoluter Pfad zum Ordner, worin die Bilder gespeichert sind.

for count, f in enumerate(os.listdir(dir)):
    f_name, f_ext = os.path.splitext(f)
    f_name = "_" + str(count+1) # einen beli
 
    new_name = f'{f_name}{f_ext}'
    os.rename(f, new_name)

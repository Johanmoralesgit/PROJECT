import shutil
from pathlib import Path

current_path = Path.cwd()

# Pedimos al usuario que ingrese el directorio a ordenar
dir_path = Path(input("Por favor ingrese la ruta del directorio a ordenar: "))

# Verificamos si el directorio existe
if dir_path.exists():
    if dir_path.is_dir():
        for file_path in dir_path.iterdir():
            # Obtenemos la extensión del archivo
            extension = file_path.suffix.lower()
            # Creamos el directorio correspondiente a la extensión, si no existe
            if not (dir_path / (extension + "s")).is_dir():
                (dir_path / (extension + "s")).mkdir()
                print(f"Carpeta {extension}s creada.")
            # Movemos el archivo al directorio correspondiente
            shutil.move(str(file_path), str(dir_path / (extension + "s") / file_path.name))
        
        print("Archivos ordenados correctamente.")
    else:
        print('Lo siento, no es posible trabajar sobre archivos.')
else:
    print("Lo siento, la ruta es incorrecta o el directorio ingresado no existe.")

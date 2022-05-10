import os

carpetas = ("Downloaders","Descargas") #Posibles formas de llamar el directorio descargas

path = f"/home/{os.getlogin()}"
for indice,carpeta in enumerate(carpetas):
    if(os.path.exists(path+"/"+carpeta)):
        path = path+"/"+carpeta
    elif(len(carpetas)==indice+1): #Comprobación del Directorio 'Descargas' sino existe muestro un mensaje de error.
        print("Error: No existe la carpeta de Descargas")
        exit(1)
        

print(f"Descargas: {path} \n")

for item in os.listdir(path):
    if os.path.isfile(path+"/"+item):
        print(item)
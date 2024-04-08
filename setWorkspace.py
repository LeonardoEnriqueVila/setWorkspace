import os
import tkinter as tk
from tkinter import simpledialog
import subprocess
import difflib

ROOT = tk.Tk()
ROOT.withdraw() # Ocultar ventana principal y evitar el mainloop

# Abstraccion que se ocupa de crear la interfaz basica y devolver el input del usuario
folderName = simpledialog.askstring(title="Set Workspace",
                                    prompt="Enter project's folder name:")

# Construye un path, "concatenando" los argumentos y agregando los / o \ segun el Sitema operativo
# en este caso, crea un path que une USERPROFILE (ruta del directorio principal del usuario) con la string Desktop
desktopPath = os.path.join(os.environ['USERPROFILE'], 'Desktop') 

# list comprehension:
# Primero itera en todos los archivos del directorio "fileName for fileName in os.listdir(desktopPath)"
# Y crea una lista con todos los nombres de archivos en el path indicado
# Luego "if os.path.isdir(os.path.join(desktopPath, fileName)" verifica cuales de esos archivos son directorios
# Usa os.path.join(desktopPath, fileName) para crear el path completo, 
# ya que "os.path.isdir" requiere de un path completo para verificar que sea un directorio
desktopFolders = [fileName for fileName in os.listdir(desktopPath) if os.path.isdir(os.path.join(desktopPath, fileName))]

def getClosestMatch():
    possibleMatchFolder = [] # lista de posibles carpetas (carpetas hijo, las que buscamos)
    possibleDesktopFolder = [] # lista de posibles carpetas de escritorio (carpetas padre, donde estan las carpetas de proyectos dentro)
    for desktopFolder in desktopFolders: # iterar en carpetas de escritorio (carpetas padre)
        desktopFolderPath = os.path.join(desktopPath, desktopFolder) # Path de la carpeta de escritorio (carpeta padre)
        # crear lista de carpetas dentro de la desktopFolder actual (carpetas hijo)
        childFolders = [fileName for fileName in os.listdir(desktopFolderPath) if os.path.isdir(os.path.join(desktopFolderPath, fileName))]
        # buscar un closestMatch entre las carpetas hijo de la carpeta padre
        closestMatch = difflib.get_close_matches(folderName, childFolders, n=1, cutoff=0.6)
        if closestMatch: # si dentro de la carpeta padre actual de la iteracion, hay una carpeta hijo que posiblemente coincida
            possibleMatchFolder.append(closestMatch[0]) # agregar el match como posible objetivo (carpeta hijo)
            possibleDesktopFolder.append([closestMatch[0], desktopFolderPath]) # asociar carpeta hijo con carpeta padre de escritorio
            # esta asociacion permitira luego obtener la carpeta padre de la carpeta hijo a la que se busca

    # una vez se recolectaron los posibles matchs, se busca un ganador
    # possibleMatchFolder es una lista de las posibles carpetas hijo que pueden ser el match
    closestMatch = difflib.get_close_matches(folderName, possibleMatchFolder, n=1, cutoff=0.6)

    # luego necesitamos obtener la carpeta padre de escritorio donde esta esa carpeta hijo que se seleccionó
    for i in range(0, len(possibleDesktopFolder)): # iteramos buscando en las posibles carpetas padre
        # possibleDesktopFolder[i][0] sera el posible match,  possibleDesktopFolder[i][1] es la carpeta padre asociada a ese match
        if possibleDesktopFolder[i][0] == closestMatch[0]: # comparamos el match con la carpeta hijo asociada a la carpeta padre actual
            return os.path.join(possibleDesktopFolder[i][1], closestMatch[0]) # creamos el path correspondiente
    return False

folderPath = getClosestMatch()
if folderPath:
    subprocess.Popen(["code", folderPath], shell=True) # ejecuta el path en la terminal usando el comando "code", replicando una apertura manual
else: 
    print("Not found")

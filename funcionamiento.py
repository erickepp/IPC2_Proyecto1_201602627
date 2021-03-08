import xml.etree.ElementTree as ET

tree = None

def cargar_archivo():
    path = input('Ingrese la ruta del archivo: ')
    if path:
        global tree
        tree = ET.parse(path)
        print('El archivo ha sido cargado con éxito')

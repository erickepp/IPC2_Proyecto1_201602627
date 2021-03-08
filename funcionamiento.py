from lista import Lista
from lista_circular import ListaCircular
from matriz import Matriz
from matriz import generar_frecuencia
from matriz import generar_binaria
import xml.etree.ElementTree as ET
import esquema_xml, time

tree = None
matrices = ListaCircular()

def cargar_archivo():
    path = input('Ingrese la ruta del archivo: ')
    if path:
        global tree
        tree = ET.parse(path)
        print('El archivo ha sido cargado con éxito')

def procesar_archivo():
    frecuencias = Lista()
    binarias = Lista()
    if tree:
        root = tree.getroot()
        for elem in root:
            if esquema_xml.validar(elem, matrices):
               frecuencias.agregar_al_final(generar_frecuencia(elem))
               matriz = Matriz(elem.attrib['nombre'])
               matrices.agregar_al_final(matriz)
    if not frecuencias.is_empty():
        print('> Calculando la matriz binaria...')
        for frecuencia in frecuencias:
            binarias.agregar_al_final(generar_binaria(frecuencia))
        time.sleep(1)
        print('> Realizando suma de tuplas...')
        posicion = 0
        for matriz in matrices:
            if matriz.datos.is_empty():
                frecuencia = frecuencias.get_valor(posicion)
                binaria = binarias.get_valor(posicion)
                matriz.sumar_tuplas(frecuencia, binaria)
                posicion += 1
        time.sleep(1)

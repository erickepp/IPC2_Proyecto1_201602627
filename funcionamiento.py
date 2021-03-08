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

def escribir_archivo_salida():
    if not matrices.is_empty():
        print('Matrices')
        for matriz in matrices:
            print('    ' + matriz.nombre)
        nombre = input('\nIngrese el nombre de la matriz: ')
        for matriz in matrices:
            if matriz.nombre == nombre:
                path = input('Escribir una ruta específica: ')
                if path:
                    matriz.generar_xml(path)
                    print('Se escribio el archivo con éxito')
                break
        else:
            print('La matriz no existe')

def mostrar_datos_estudiante():
    print('> Erick Estuardo Patzan Polanco')
    print('> 201602627')
    print('> Introducción a la Programación y Computación 2 Sección "C"')
    print('> Ingeniería en Ciencias y Sistemas')
    print('> 4to Semestre')

def generar_grafica():
    if not matrices.is_empty():
        print('Matrices')
        for matriz in matrices:
            print('    ' + matriz.nombre)
        nombre = input('\nIngrese el nombre de la matriz: ')
        for matriz in matrices:
            if matriz.nombre == nombre:
                print('> Generando gráfica...')
                matriz.generar_grafica()
                break
        else:
            print('La matriz no existe')

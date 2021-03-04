from lista import Lista
from graphviz import Digraph
from xml.dom import minidom
import xml.etree.ElementTree as ET

class Matriz:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__grupos = Lista()
        self.__datos = Lista()
        self.__filas = 0
        self.__columnas = 0

    def __calcular_dimensiones(self):
        self.__filas = self.__datos.get_tamanio()
        self.__columnas = self.__datos.get_valor(0).get_tamanio()

    def __generar_grupos(self, frecuencia, binaria):
        posiciones = Lista()
        filas = binaria.get_tamanio()
        for i in range(filas):
            if not (i in posiciones):
                grupo = Lista()
                posiciones.agregar_al_final(i)
                grupo.agregar_al_final(frecuencia.get_valor(i))
                cadena = ''.join(map(str, binaria.get_valor(i)))
                for j in range(i + 1, filas):
                    if cadena == ''.join(map(str, binaria.get_valor(j))):
                        posiciones.agregar_al_final(j)
                        grupo.agregar_al_final(frecuencia.get_valor(j))
                self.__grupos.agregar_al_final(grupo)

    def sumar_tuplas(self, frecuencia, binaria):
        self.__generar_grupos(frecuencia, binaria)
        columnas = self.__grupos.get_valor(0).get_valor(0).get_tamanio()
        for grupo in self.__grupos:
            nueva_tupla = Lista()
            for i in range(columnas):
                suma = 0
                for tupla in grupo:
                    suma += tupla.get_valor(i)
                nueva_tupla.agregar_al_final(suma)
            self.__datos.agregar_al_final(nueva_tupla)
        self.__calcular_dimensiones()

    def generar_xml(self, path):
        matriz = ET.Element('matriz')
        matriz.set('nombre', self.__nombre + '_Salida')
        matriz.set('n', str(self.__filas))
        matriz.set('m', str(self.__columnas))
        matriz.set('g', str(self.__grupos.get_tamanio()))

        for fila in self.__datos:
            n_fila = self.__datos.get_posicion(fila) + 1
            n_columna = 1
            for columna in fila:
                dato = ET.SubElement(matriz, 'dato')
                dato.set('x', str(n_fila))
                dato.set('y', str(n_columna))
                dato.text = str(columna)
                n_columna += 1
        for grupo in self.__grupos:
            n_grupo = self.__grupos.get_posicion(grupo) + 1
            frecuencia = ET.SubElement(matriz, 'frecuencia')
            frecuencia.set('g', str(n_grupo))
            frecuencia.text = str(grupo.get_tamanio())

        dom = minidom.parseString(ET.tostring(matriz, 'utf-8'))
        with open(path, 'w') as f:
            f.write(dom.toprettyxml())

    def generar_grafica(self):
        g = Digraph('G', filename='grafica.gv', format='png')
        g.edge('Matrices', self.__nombre)
        g.attr('node', shape='doublecircle', color='blue')
        g.edge(self.__nombre, 'n = ' + str(self.__filas))
        g.edge(self.__nombre, 'm = ' + str(self.__columnas))
        g.attr('node', shape='oval', color='black')

        for fila in self.__datos:
            n_fila = self.__datos.get_posicion(fila)
            n_columna = 0
            for columna in fila:
                g.node(str(n_fila) + str(n_columna), label=str(columna))
                n_columna += 1
        for i in range(self.__columnas):
            for j in range(self.__filas):
                if j == 0:
                    g.edge(self.__nombre, str(j) + str(i))
                else:
                    g.edge(str(j - 1) + str(i), str(j) + str(i))
        g.view()


def generar_frecuencia(elem):
    frecuencia = Lista()
    for i in range(int(elem.attrib['n'])):
        fila = Lista()
        for j in range(int(elem.attrib['m'])):
            fila.agregar_al_final(0)
        frecuencia.agregar_al_final(fila)
    for subelem in elem:
        n_fila = int(subelem.attrib['x']) - 1
        n_columna = int(subelem.attrib['y']) - 1
        dato = int(subelem.text)
        if dato != 0:
            fila = frecuencia.get_valor(n_fila)
            fila.editar_por_posicion(n_columna, dato)
    return frecuencia


def generar_binaria(frecuencia):
    binaria = Lista()
    for fila in frecuencia:
        fila_binaria = Lista()
        for columna in fila:
            if columna != 0:
                fila_binaria.agregar_al_final(1)
            else:
                fila_binaria.agregar_al_final(columna)
        binaria.agregar_al_final(fila_binaria)
    return binaria

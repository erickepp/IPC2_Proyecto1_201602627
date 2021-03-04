from lista import Lista

class Matriz:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__grupos = Lista()
        self.__datos = Lista()
        self.__filas = 0
        self.__columnas = 0

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

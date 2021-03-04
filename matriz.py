from lista import Lista

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
    for fina in frecuencia:
        fila_binaria = Lista()
        for columna in fila:
            if columna != 0:
                fila_binaria.agregar_al_final(1):
            else:
                fila_binaria.agregar_al_final(columna)
        binaria.agregar_al_final(fila_binaria)
    return binaria

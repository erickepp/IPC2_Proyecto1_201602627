from lista_circular import ListaCircular

def validar_etiqueta_matriz(elem, nombre):
    if elem.tag != 'matriz':
        print(f'Error: <{elem.tag} nombre="{nombre}">')
        print('La ubicación de la etiqueta no es válida\n')
        return False
    return True

def validar_nombre_matriz(matrices, nombre):
    for matriz in matrices:
        if matriz.nombre == nombre:
            print(f'Error: <matriz nombre="{nombre}">')
            print('La matriz ya existe\n')
            return False
        return True

def validar_atributos_matriz(elem, nombre):
    filas = elem.attrib['n']
    columnas = elem.attrib['m']
    if not filas.isdigit():
        print(f'Error: <matriz nombre="{nombre}" n="{filas}">')
        print('El atributo "n" no es válido\n')
        return False
    elif not columnas.isdigit():
        print(f'Error: <matriz nombre="{nombre}" m="{columnas}">')
        print('El atributo "m" no es válido\n')
        return False
    return True

def validar_etiquetas_dato(elem, nombre):
    for subelem in elem:
        if subelem.tag != 'dato':
            print(f'Error: <{subelem.tag} nombre="{nombre}">')
            print('La ubicación de la etiqueta no es válida\n')
            return False
    return True

def validar_atributos_dato(elem, nombre):
    for subelem in elem:
        fila = subelem.attrib['x']
        columna = subelem.attrib['y']
        if not fila.isdigit():
            print(f'Error: <matriz nombre="{nombre}"><dato x="{fila}">')
            print('El atributo "x" no es válido\n')
            return False
        elif not columna.isdigit():
            print(f'Error: <matriz nombre="{nombre}"><dato y="{columna}">')
            print('El atributo "y" no es válido\n')
            return False
    return True

def validar_contenido_dato(elem, nombre):
    for subelem in elem:
        if not subelem.text.isdigit():
            print(f'Error: <matriz nombre="{nombre}">')
            print(f'El dato "{subelem.text}" no es válido\n')
            return False
    return True

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

def validar_atributos_datos(elem, nombre):
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

def validar_contenido_datos(elem, nombre):
    for subelem in elem:
        if not subelem.text.isdigit():
            print(f'Error: <matriz nombre="{nombre}">')
            print(f'El dato "{subelem.text}" no es válido\n')
            return False
    return True

def validar_dimensiones_matriz(elem, nombre):
    filas = int(elem.attrib['n'])
    columnas = int(elem.attrib['m'])
    dimensiones = filas * columnas
    if len(elem) != dimensiones:
        print(f'Error: <matriz nombre="{nombre}" n="{filas}" m="{columnas}">')
        print('La matriz no cumple con las dimensiones (n, m)\n')
        return False
    return True

def validar_rango_dimensiones(elem, nombre):
    filas = int(elem.attrib['n'])
    columnas = int(elem.attrib['m'])
    for subelem in elem:
        fila = int(subelem.attrib['x'])
        columna = int(subelem.attrib['y'])
        if not fila in range(1, filas + 1):
            print(f'Error: <matriz nombre="{nombre}"><dato x="{fila}">')
            print('El atributo "x" está fuera de rango\n')
            return False
        elif not columna in range(1, columnas + 1):
            print(f'Error: <matriz nombre="{nombre}"><dato x="{columna}">')
            print('El atributo "y" está fuera de rango\n')
            return False
    return True

def validar(elem, matrices):
    nombre = elem.attrib['nombre']
    if not validar_etiqueta_matriz(elem, nombre):
        return False
    elif not validar_nombre_matriz(matrices, nombre):
        return False
    elif not validar_atributos_matriz(elem, nombre):
        return False
    elif not validar_etiquetas_dato(elem, nombre):
        return False
    elif not validar_atributos_datos(elem, nombre):
        return False
    elif not validar_contenido_datos(elem, nombre):
        return False
    elif not validar_dimensiones_matriz(elem, nombre):
        return False
    elif not validar_rango_dimensiones(elem, nombre):
        return False
    return True

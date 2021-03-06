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

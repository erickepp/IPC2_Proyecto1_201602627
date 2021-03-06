def validar_etiqueta_matriz(elem, nombre):
    if elem.tag != 'matriz':
        print(f'Error: <{elem.tag} nombre="{nombre}">')
        print('La ubicación de la etiqueta no es válida\n')
        return False
    return True

class ListaCircular:
    def __init__(self):
        self.__inicio = None
        self.__fin = None
        self.__tamanio = 0

    def is_empty(self):
        return self.__inicio is None

    def get_tamanio(self):
        return self.__tamanio

    def agregar_al_final(self, valor):
        nuevo = self.__Nodo(valor)
        if self.is_empty():
            self.__inicio = nuevo
            self.__fin = nuevo
        else:
            self.__fin.siguiente = nuevo
            nuevo.siguiente = self.__inicio
            self.__fin = nuevo
        self.__tamanio += 1

    def get_valor(self, posicion):
        if posicion >= 0 and posicion < self.__tamanio:
            if posicion == 0:
                return self.__inicio.valor
            else:
                aux = self.__inicio.valor
                for i in range(posicion):
                    aux = aux.siguiente
                return aux.valor
        else:
            raise IndexError('list index out of range')

    class __Nodo:
        def __init__(self, valor):
            self.valor = valor
            self.siguiente = self

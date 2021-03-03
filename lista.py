class Lista:
    def __init__(self):
        self.__inicio = None
        self.__tamanio = 0

    def is_empty(self):
        return self.__inicio is None

    def get_tamanio(self):
        return self.__tamanio

    def agregar_al_final(self, valor):
        nuevo = self.__Nodo(valor)
        if self.is_empty():
            self.__inicio = nuevo
        else:
            aux = self.__inicio
            while aux.siguiente is not None:
                aux = aux.siguiente
            aux.siguiente = nuevo
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

    def buscar(self, referencia):
        aux = self.__inicio
        encontrado = False
        while aux is not None and not encontrado:
            if referencia == aux.valor:
                encontrado = True
            else:
                aux = aux.siguiente
        return encontrado        

    def get_posicion(self, referencia):
        if self.buscar(referencia):
            aux = self.__inicio
            cont = 0
            while referencia != aux.valor:
                cont += 1
                aux = aux.siguiente
            return cont
        else:
            raise IndexError('list index out of range')

    def editar_por_posicion(self, posicion, valor):
        if posicion >=0 and posicion < self.__tamanio:
            if posicion == 0:
                self.__inicio.valor = valor
            else:
                aux = self.__inicio
                for i in range(posicion):
                    aux = aux.siguiente
                aux.valor = valor

    def __iter__(self):
        actual = self.__inicio
        while actual is not None:
            yield actual.valor
            actual = actual.siguiente

    class __Nodo:
        def __init__(self, valor):
            self.valor = valor
            self.siguiente = None

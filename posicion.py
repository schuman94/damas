class Posicion:
    def __init__(self, fila, columna):
        self.__fila = fila
        self.__columna = columna

    def get_fila(self):
        return self.__fila

    def get_columna(self):
        return self.__columna

    def __str__(self):
        return f'{self.get_fila()}, {self.get_columna()}'

    def __repr__(self):
        return f'Posicion({self.get_fila()}, {self.get_columna()})'

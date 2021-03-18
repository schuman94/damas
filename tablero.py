from ficha import Ficha
from posicion import Posicion

class Tablero:
    patron_blanco = ((1, 1), (1, 3), (1, 5), (1, 7),
                     (2, 2), (2, 4), (2, 6), (2, 8),
                     (3, 1), (3, 3), (3, 5), (3, 7))

    patron_negro = ((8, 2), (8, 4), (8, 6), (8, 8),
                    (7, 1), (7, 3), (7, 4), (7, 6),
                    (6, 2), (6, 4), (6, 6), (6, 8))

    def __init__(self):
        self.__contenido = {}
        self.__colocar_fichas('B')
        self.__colocar_fichas('N')

    def __colocar_fichas(self, color):
        if color == 'B':
            patron = Tablero.patron_blanco
        elif color == 'N':
            patron = Tablero.patron_negro
        else:
            raise ValueError('Color incorrecto')

        num_ficha = 0

        while num_ficha < 12:
            fila = patron[num_ficha][0]
            columna = patron[num_ficha][1]
            self.__contenido[Posicion(fila, columna)] = Ficha(color)
            num_ficha += 1

    def imprimir_contenido(self):
        print(self.__contenido)

class Ficha:
    def __init__(self, color):
        self.__set_color(color)

    def __set_color(self, color):
        if color not in ('B', 'N'):
            raise ValueError('Las fichas solo pueden ser blancas o negras')
        self.__color = color

    def get_color(self):
        return self.__color

    def __str__(self):
        return f'Ficha_{self.get_color()}'

    def __repr__(self):
        return 'Ficha(' + '\'' + self.get_color() + '\'' + ')'

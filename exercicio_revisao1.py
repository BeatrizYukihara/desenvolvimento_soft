

class Bebida:

    def __init__(self, quantidade, ingredientes, temperatura, nome, codigo_fabricante, alcolico):
        self.quantidade = quantidade
        self.ingredientes = ingredientes
        self.temperatura = temperatura
        self.nome = nome
        self.alcolico = alcolico
        self.__codigo_fabricante = codigo_fabricante

    def __str__(self):
        if self.alcolico == True:
            return (f'A bebida {self.nome}, tem {self.quantidade}mls, foi feita com {self.ingredientes}, é servida {self.temperatura} e é alcolica.')
        else:
            return (f'A bebida {self.nome}, tem {self.quantidade}mls, foi feita com {self.ingredientes}, é servida {self.temperatura} e não é alcolica.')

    def get_codigo(self):
        print(f'O código do fabricante é {self.__codigo_fabricante}')

if "__main__":
    bebida1 = Bebida(200, 'abacaxi e menta', 'gelada', 'suco de abacaxi com menta', 11111111, False)
    bebida2 = Bebida(250, 'laranja e morango', 'gelada', 'suco de laranja com menta', 9999999, True)
    print(bebida1)
    print(bebida2)
    bebida1.get_codigo()
    bebida2.get_codigo()
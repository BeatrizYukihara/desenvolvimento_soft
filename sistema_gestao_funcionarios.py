from abc import ABC,abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.hora_extra = False
        lista_func = []

    def cadastrar_funcionario(self, funcionario):
        


        '''if funcionario == True:
            self.lista_f.append(funcionario)'''
       
    @abstractmethod
    def calcular_salario(self):
        pass

    @abstractmethod
    def show_info(self):
        pass


class Administrativos(Funcionario):
    def __init__(self, nome, cpf, salario, ):
        super().__init__(nome, cpf, salario)
        


    def calcular_salario(self,):
        pass


class Professores(Funcionario):
    def __init__(self, nome, cpf, salario, disciplina):
        super().__init__(nome, cpf, salario)
        self.disciplina = disciplina

    def calcular_salario():
        pass


class Tecnicos(Funcionario):
    def __init__(self, nome, cpf, salario, area_atuacao):
        super().__init__(nome, cpf, salario)
        self.area_ateacao = area_atuacao

    def calcular_salario():
        pass

print('oi')
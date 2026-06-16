from datetime import date
class cliente:
    def __init__(self, nome:str, data_nascimento: date, cpf:str):
        self.nome= nome
        self.data_nascimento= data_nascimento
        self.cpf= cpf

class pedido:
    def __init__(self, )
from datetime import date
class cliente:
    def __init__(self, nome:str, data_nascimento: date, cpf:str):
        self.nome= nome
        self.data_nascimento= data_nascimento
        self.cpf= cpf

class pedido:
    def __init__(self, data_pedido:date, percentual_desconto:float, valor_final:float, cliente:cliente, pratos:list):
        self.data_pedido=data_pedido
        self.percentual_desconto= percentual_desconto
        self.valor_final= valor_final
        self.cliente= cliente
        self.pratos= pratos

class prato:
    def __init__ (self, nome:str, ingredientes:list[str], modo_preparo:str, preco:float):
        self.nome=nome
        self.ingredientes=ingredientes
        self.modo_preparo=modo_preparo
        self.preco=preco

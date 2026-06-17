from datetime import date
class cliente:
    def __init__(self, nome:str, data_nascimento: date, cpf:str):
        self.nome= nome
        self.data_nascimento= data_nascimento
        self.cpf= cpf

class pedido:
    def __init__(self, data_pedido:date, percentual_desconto:float, valor_final:float, cliente:cliente, itens:list):
        self.data_pedido=data_pedido
        self.percentual_desconto= percentual_desconto
        self.valor_final= valor_final
        self.cliente= cliente
        self.itens= itens
class prato:
    def __init__ (self, nome:str, ingredientes:list[str], modo_preparo:str, preco:float):
        self.nome=nome
        self.ingredientes=ingredientes
        self.modo_preparo=modo_preparo
        self.preco=preco

class itemdopedido:
    def __init__(self, prato:prato, valor_prato:str, quantidade:int):
        self.prato=prato
        self.valor_prato=valor_prato
        self.quantidade=quantidade

c1= cliente("Roberto", date(1984, 4, 23), "9018867")
pra1= prato("Lasanha", ["massa", "carne"], "Assa a lasanha no forno", 200.10)
pra2= prato("Pizza", ["carne", "massa"], "Pizza nhum nhum", 40)
it1= (pra1, 200.10, 1)
it2= (pra2, 40, 2)
pe1= pedido(date(2021, 5, 12), 2, c1, [it1, it2])


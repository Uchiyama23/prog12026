class veiculo:
    def __init__(self, placa:str, ano:int):
        self.placa=placa
        self.ano= ano

class moto(veiculo):
    def __int__(self, placa:str, ano:str):
        super().__init__(placa, ano)

class caminhao(veiculo):
    def __init__(self, placa:str, ano:str, peso_em_kg:int):
        super().__init__(placa, ano)
        self.peso_em_kg= peso_em_kg

m1= moto("AB123", 2011)
C1= caminhao("CD123", 2020, 75)
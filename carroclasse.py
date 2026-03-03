# Herança: a classe Automotivo herdou as características de Veiculo e adicionou uma extra

class Veiculo:
    def __init__(self, cor: str, ano: int):
        self.cor = cor
        self.ano = ano


class Automotivo(Veiculo):
    def __init__(self, cor: str, ano: int, modelo: str):
        super().__init__(cor, ano)
        self.modelo = modelo

    def qualquer(self, q) -> bool:
        self.q = q
        return q > 10


auto1 = Automotivo("Vermelho", "2004", "Subaru Impreza")

print(f"""
       {auto1.cor},
       {auto1.ano},
       {auto1.modelo}
 """)

# print(f"{auto1.qualquer(10)}")

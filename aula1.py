# class Cpf:
#     def __init__(self, nome, numero):
#         self.nome = nome
#         self.numero = numero
        
#     def status(self):
#         return f"{self.nome} e {self.numero}"


# aluno = Cpf("Vinicius", 123456789)
# print(f'{aluno.status()}')


# class Gato:
#     def __init__(self, nome, cor):
#         self.nome = nome
#         self.cor = cor
        
#     def falar(self):
#         return f"Miau"
    
#     def comer(self):
#         return f"Comeu ração"
    
#     def dormir(self):
#         return f"Dormiu"
    
# meu_gato = Gato("Romeu", "Preto")

# print(f"Meu gato faz {meu_gato.falar()} e agora ele {meu_gato.dormir()}")


# class Veiculo:
#     def __init__(self, modelo, cor, ano):
#         self.modelo = modelo
#         self.cor = cor
#         self.ano = ano
    
# veiculo1 = Veiculo("Subaru Impreza", "Azul", 2000)
# print(f"""{veiculo1.modelo}
# {veiculo1.cor}
# {veiculo1.ano}
# """)


# Cálculo de área
class Objeto:
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2
    
    def area(self, lado1, lado2):
        return lado1 * lado2
        
    
print("Digite o lado 1 do retângulo")
        
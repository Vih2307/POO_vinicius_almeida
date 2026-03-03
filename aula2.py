class Ninja:
    def __init__(self, nacao, vila):
        self.nacao = nacao
        self.vila = vila

    def atacar(self):
        print("Jogar shuriken!!")

    def defender(self):
        print("Jutsu substituicao!!")


class Lutador(Ninja):
    def __init__(self, nacao, vila, especialidade):
        super().__init__(nacao, vila)
        self.especialidade = especialidade


# n1 = Ninja("fogo", "folha")

# print(f"De onde veio o ninja? {n1.nacao} e {n1.vila}")
# n1.atacar()
# print(f"{n1.defender()}")

# a1 = Lutador("Montanha", "folha", "agua")

# print(
#     f"De onde veio o ninja? {a1.nacao} e {a1.vila} e sua especialidade eh {a1.especialidade}")

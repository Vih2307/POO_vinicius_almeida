class Livro:
    def __init__(self, isnb: str, titulo: str, autor: str, disponivel: bool):
        self.isnb = isnb
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O livro {self.titulo} foi emprestado")
        else:
            print(f"O livro {self.titulo} não pode ser emprestado")

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"O livro {self.titulo} foi devolvido")
        else:
            print(f"O livro {self.titulo} já estava disponível no sistema")


class Usuario:
    def __init__(self, matricula: str, nome: str, lista_livro_emprestado: list):
        self.matricula = matricula
        self.nome = nome
        self.lista_livro_emprestado = lista_livro_emprestado

    def pegar_emprestado(self):
        pass

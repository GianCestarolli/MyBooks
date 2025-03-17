from models.livros.livro import Livro

class Dropado(Livro):
    livros_dropados = []
    def __init__(self, nome, autor, motivo):
        super().__init__(nome, autor)
        self.motivo = motivo
        Dropado.livros_dropados.append(self)

    @classmethod
    def listarDropados(cls):
        for livro in cls.livros_dropados:
            print (f'\n{livro.nome} | Autor: {livro.autor} | Motivo: {livro.motivo}\n')

    
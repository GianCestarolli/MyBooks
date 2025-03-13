from models.livro import Livro

class Finalizado(Livro):
    livros_finalizados = []
    def __init__(self, nome, autor, ano, minha_nota):
        super().__init__(nome, autor, ano)
        self._minha_nota = minha_nota
        Finalizado.livros_finalizados.append(self)
    
    def __str__(self):
        return super().__str__() + f'  {self._minha_nota}'
    
    @classmethod
    def listar_finalizados(cls):
        for livro in cls.livros_finalizados:
            print (f'\n{livro._nome} | Autor: {livro._autor} | Ano de lançamento: {livro._ano} | Minha nota: {livro._minha_nota}\n')
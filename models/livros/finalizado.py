from models.livros.livro import Livro

class Finalizado(Livro):
    livros_finalizados = []
    def __init__(self, nome, autor, minha_nota):
        super().__init__(nome, autor)
        self.minha_nota = minha_nota
        Finalizado.livros_finalizados.append(self)
    
    def __str__(self):
        return super().__str__() + f'  {self._minha_nota}'
    
    @classmethod
    def listarFinalizados(cls):
        for livro in cls.livros_finalizados:
            print (f'\n{livro.nome} | Autor: {livro.autor} | Minha nota: {livro.minha_nota}\n')

    

    
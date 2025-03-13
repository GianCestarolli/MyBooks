from models.livro import Livro

class Finalizado(Livro):
    def __init__(self, nome, autor, ano, minha_nota):
        super().__init__(nome, autor, ano)
        self._minha_nota = minha_nota
    
    def __str__(self):
        return super().__str__() + f'  {self._minha_nota}'
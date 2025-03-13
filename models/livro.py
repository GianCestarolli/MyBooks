class Livro:
    def __init__(self, nome, autor, ano):
        self._nome = nome
        self._autor = autor
        self._ano = ano
    
    def __str__(self):
        return f'{self._nome} | {self._autor} | {self._ano}'
        
        
class Livro:
    def __init__(self, nome, autor):
        self._nome = nome
        self._autor = autor
    
    def __str__(self):
        return f'{self._nome} | {self._autor}'
        
        
class Livro:
    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor
    
    def __str__(self):
        return f'{self.nome} | {self.autor}'
    
        
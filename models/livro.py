class Livro:
    def __init__(self, nome, autor, data, andamento):
        self._nome = nome
        self._autor = autor
        self._data = data
        self._andamento = andamento
    
    def __str__(self):
        return f'{self._nome} | {self._autor} | {self._data} | {self._andamento}'
        
from models.finalizados import Finalizado

class Registros:
    def registrarLivro():
        from models.sistema import Sistema
        nomeLivro = input("Digite o nome do livro: ")
        autorLivro = input("Digite o autor: ")
        anoLivro = input("Digite o ano de lançamento: ")
        notaLivro = input("Digite sua nota: ")
        Finalizado(nomeLivro, autorLivro, anoLivro, notaLivro)
        print("Livro registrado com sucesso!\n")
        input("Digite qualquer coisa para retornar: ")
        Sistema.menu()
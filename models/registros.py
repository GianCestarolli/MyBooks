from models.livros.finalizado import Finalizado
import os

class Registros:
    def registrarLivro():
        from models.sistema import Sistema
        os.system("cls")
        nomeLivro = input("Digite o nome do livro: ")
        autorLivro = input("Digite o autor: ")
        notaLivro = input("Digite sua nota: ")
        Finalizado(nomeLivro, autorLivro, notaLivro)
        os.system("cls")
        print("Livro registrado com sucesso!\n")
        input("Digite qualquer coisa para retornar: ")
        os.system("cls")
        Sistema.menu()
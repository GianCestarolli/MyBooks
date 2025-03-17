from models.livros.finalizado import Finalizado
from models.livros.dropado import Dropado
import os

class Registros:
    def registrarFinalizado():
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

    def registrarDropado():
        from models.sistema import Sistema
        os.system("cls")
        nomeLivro = input("Digite o nome do livro: ")
        autorLivro = input("Digite o autor: ")
        motivoDrop = input("Digite o motivo do drop: ")
        Dropado(nomeLivro, autorLivro, motivoDrop)
        os.system("cls")
        print("Livro registrado com sucesso!\n")
        input("Digite qualquer coisa para retornar: ")
        os.system("cls")
        Sistema.menu()
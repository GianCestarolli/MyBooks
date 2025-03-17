from models.registros import Registros

class Sistema:
    def menu():
        print("Bem vindo ao MyBooks!\n")
        print("1. Registrar livros\n"
              "2. Listar livros\n")
        resposta = input("Escolha uma opção: ")
        if resposta == "1":
            Registros.registrarLivro()
            
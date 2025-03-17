import os
from models.registros import Registros
from models.livros.finalizado import Finalizado


class Sistema:
    def menu():
        print("Bem vindo ao MyBooks!\n")
        print("1. Registrar livro finalizado\n"
              "2. Listar livros\n"
              "3. Registrar livro dropado\n")
        resposta = input("Escolha uma opção: ")
        if resposta == "1":
            Registros.registrarLivro()
        elif resposta == "2":
            os.system("cls")
            Finalizado.listar_finalizados()
            
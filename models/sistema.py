import os
from models.registros import Registros
from models.finalizados import Finalizado


class Sistema:
    def menu():
        print("Bem vindo ao MyBooks!\n")
        print("1. Registrar livros\n"
              "2. Listar livros\n")
        resposta = input("Escolha uma opção: ")
        if resposta == "1":
            Registros.registrarLivro()
        elif resposta == "2":
            os.system("cls")
            Finalizado.listar_finalizados()
            
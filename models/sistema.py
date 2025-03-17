import os
from models.registros import Registros
from models.livros.finalizado import Finalizado
from models.livros.dropado import Dropado

class Sistema:
    def menu():
        print("Bem vindo ao MyBooks!\n")
        print("1. Registrar livro finalizado\n"
              "2. Listar livros\n"
              "3. Registrar livro dropado\n"
              "4. Listar livros dropados\n")
        resposta = input("Escolha uma opção: ")
        if resposta == "1":
            Registros.registrarFinalizado()
        elif resposta == "2":
            os.system("cls")
            Finalizado.listarFinalizados()
        elif resposta == "3":
            Registros.registrarDropado()
        elif resposta == "4":
            Dropado.listarDropados()
        
            
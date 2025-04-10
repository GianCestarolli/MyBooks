import os
import json
from models.livros.finalizado import Finalizado
from models.livros.dropado import Dropado

class Registros:
    def registrarFinalizado():
        from models.sistema import Sistema
        os.system("cls")
        nomeLivro = input("Digite o nome do livro: ")
        autorLivro = input("Digite o autor: ")
        notaLivro = input("Digite sua nota: ")
        Finalizado(nomeLivro, autorLivro, notaLivro)
        Registros.salvar_finalizados()
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
        Registros.salvar_dropados()
        os.system("cls")
        print("Livro registrado com sucesso!\n")
        input("Digite qualquer coisa para retornar: ")
        os.system("cls")
        Sistema.menu()

    def salvar_finalizados():
        # Lê o arquivo JSON existente, se houver, para preservar os dados anteriores
        try:
            with open("livros_finalizados.json", "r") as arquivo:
                data_finalizados = json.load(arquivo)
        except (FileNotFoundError, json.JSONDecodeError):
            # Caso o arquivo não exista ou esteja vazio, inicializa com uma lista vazia
            data_finalizados = []

        # Adiciona os livros registrados na lista de dados
        for livro in Finalizado.livros_finalizados:
            data_finalizados.append({
                "nome": livro.nome,
                "autor": livro.autor,
                "nota": livro.minha_nota
            })
        
        # Escreve a lista de dados atualizada no arquivo JSON
        with open("livros_finalizados.json", "w") as arquivo:
            json.dump(data_finalizados, arquivo, indent=4)

    def salvar_dropados():
        # Lê o arquivo JSON existente, se houver, para preservar os dados anteriores
        try:
            with open("livros_dropados.json", "r") as arquivo:
                data_dropados = json.load(arquivo)
        except (FileNotFoundError, json.JSONDecodeError):
            # Caso o arquivo não exista ou esteja vazio, inicializa com uma lista vazia
            data_dropados = []

        # Adiciona os livros registrados na lista de dados
        for livro in Dropado.livros_dropados:
            data_dropados.append({
                "nome": livro.nome,
                "autor": livro.autor,
                "motivo": livro.motivo
            })
        
        # Escreve a lista de dados atualizada no arquivo JSON
        with open("livros_dropados.json", "w") as arquivo:
            json.dump(data_dropados, arquivo, indent=4)




from models.finalizados import Finalizado

o_hobbit = Finalizado("O Hobbit", "J.R Tolkien", 1937, 8.0)
o_livro_dos_cinco_aneis = Finalizado("O livro dos cinco anéis", "Miyamoto Musashi", 1645, 8.5)


def main():
    Finalizado.listar_finalizados()

if __name__ == '__main__':
    main()
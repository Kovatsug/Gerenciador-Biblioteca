from livro import Livro
from pessoas import Leitor
from abc import ABC, abstractmethod

class Operacoes(ABC):
    
    def listar_livros(livros):
        if livros == []:
            print("Nenhum livro cadastrado.")
        for livro in livros:
            print(livro)

    @abstractmethod
    def emprestar_livro(livros, pessoas):
        pass

    @abstractmethod
    def devolver_livro(livros, pessoas):
        pass

class Operacoes_Leitor(Operacoes):


    def emprestar_livro(livros, pessoas, id_leitor):
        try:
            titulo = input("Titulo do livro: ")
            for l in livros:
                if l.titulo == titulo:
                    livro = l
                    break
            for p in pessoas:
                if p.id == id_leitor:
                    leitor = p
                    break
            livro.emprestar(leitor)
            print("Livro emprestado com sucesso!")
        except Exception as e:
            print(f"Erro: {e}")
    
    def devolver_livro(livros, pessoas, id_leitor):
        try:
            titulo = input("Titulo do livro: ")
            for p in pessoas:
                if p.id == id_leitor:
                    leitor = p
                    break
            for l in livros:
                if l.titulo == titulo and l.emprestado_para == leitor.nome:
                    livro = l
                    break
            livro.devolver(leitor)
            print("Livro devolvido com sucesso!")
        except Exception as e:
            print(f"Erro: {e}")


class Operacoes_Administrador(Operacoes):

    def emprestar_livro(livros, pessoas):
        try:
            titulo = input("Titulo do livro: ")
            
            id_pessoa = input("ID da pessoa: ")
            for l in livros:
                if l.titulo == titulo:
                    livro = l
                    break
            for p in pessoas:
                if p.id == id_pessoa:
                    pessoa = p
                    break
            livro.emprestar(pessoa)
            print("Livro emprestado com sucesso!")
        except Exception as e:
            print(f"Erro: {e}")

    def devolver_livro(livros, pessoas):
        try:
            id_pessoa = input("ID da pessoa: ")
            for p in pessoas:
                if p.id == id_pessoa:
                    pessoa = p
                    break
            titulo = input("Titulo do livro: ")
            for l in livros:
                if str(l.titulo) == titulo and l.emprestado_para == pessoa.nome:
                    livro = l
                    break
            livro.devolver(pessoa)
            print("Livro devolvido com sucesso!")
        except Exception as e:
            print(f"Erro: {e}")

     #Exclusivo Administrador

    def cadastrar_livro(livros):
        try:
            titulo = input("Título: ")
            autor = input("Autor: ")
            disponivel = True
            emprestado_para = None
            livro = Livro(titulo, autor, disponivel, emprestado_para)
            livros.append(livro)
            print("Livro cadastrado com sucesso!")
        except Exception as e:
            print(f"Erro: {e}")

    def excluir_livro(livros,pessoas):
        try:
            titulo = input("Título do livro a ser excluído: ")
            for l in livros:
                if l.titulo == titulo:
                    livro = l
            livros.remove(livro)
            for p in pessoas:
                if p.nome == livro.emprestado_para:
                    p.livros_emprestados.remove(livro.titulo)
            print("Livro excluído com sucesso!")
        except StopIteration:
            print("Livro não encontrado.")
        except Exception as e:
            print(f"Erro: {e}")

    def cadastrar_leitor(pessoas):
        nome = input("Nome do leitor: ")
        leitor_id = f"{len(pessoas):03d}"
        admin = False
        livros_emprestados = []
        leitor = Leitor(nome, leitor_id, admin, livros_emprestados)
        pessoas.append(leitor)
        print("Leitor cadastrado com sucesso!")

    def listar_leitores(pessoas):
        if not pessoas:
            print("Nenhum leitor cadastrado.")
        for p in pessoas[1:]:  # Ignorando o root
            print(p)
            print("\n-----------------\n")

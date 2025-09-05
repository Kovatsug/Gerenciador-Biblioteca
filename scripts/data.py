import pandas as pd 
import os
import ast
from livro import Livro
from pessoas import Leitor

def carregar_dados():
    try:
        l_path='data/livros.csv'

        # Verifica se o diretório existe, se não, cria
        if not os.path.exists('data'):
            os.makedirs('data')

        if not os.path.exists(l_path):
            colunas = ['titulo', 'autor', 'disponivel', 'emprestado_para']
            df_livros = pd.DataFrame(columns=colunas)
            df_livros.to_csv(l_path, index=False)

        df_livros = pd.read_csv(l_path)
    
        # Recriando objetos Livro
        livros = [Livro(
            str(row.titulo),
            str(row.autor),
            (row.disponivel),
            str(row.emprestado_para)
        ) for row in df_livros.itertuples()]

        p_path='data/leitores.csv'
        
        if not os.path.exists(p_path):
            leitor_data={"id":"000","nome":"root","admin":True,"livros_emprestados":[]}
            df_pessoas=pd.DataFrame([leitor_data])
            df_pessoas.to_csv(p_path, index=False)

        df_pessoas = pd.read_csv(p_path)

        # Recriando objetos Leitor
        pessoas = [Leitor(
            str(row.nome),
            f"{row.id:03d}",
            (row.admin),
            ast.literal_eval(row.livros_emprestados)
        ) for row in df_pessoas.itertuples()]
        return livros, pessoas
    
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")


def salvar_dados(livros, pessoas):
    try:
        if livros:
            df_livros = pd.DataFrame([livro.__dict__ for livro in livros])
        else:
            colunas = ['titulo', 'autor', 'disponivel', 'emprestado_para']
            df_livros = pd.DataFrame(columns=colunas)
            
        df_pessoas = pd.DataFrame([pessoa.to_dict() for pessoa in pessoas])
        df_livros.to_csv('data/livros.csv', index=False)
        df_pessoas.to_csv('data/leitores.csv', index=False)

    except Exception as e:
        print(f"Erro ao salvar dados: {e}")

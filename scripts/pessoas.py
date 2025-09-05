from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome):
        self.nome = nome


class Leitor(Pessoa):
    def __init__(self, nome, id, admin, livros_emprestados):
        super().__init__(nome)
        self.__id = id
        self.__admin = admin
        self.livros_emprestados = livros_emprestados

    @property
    def id(self):
        return self.__id
    @property
    def admin(self):
        return self.__admin


    def __str__(self):

        return f"Leitor: {self.nome}, ID: {self.id}, Livros Emprestados: {self.livros_emprestados}"

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'admin': self.admin,
            'livros_emprestados': [livro for livro in self.livros_emprestados]
        }




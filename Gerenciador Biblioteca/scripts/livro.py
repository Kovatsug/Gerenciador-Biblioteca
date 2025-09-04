class Livro:
    def __init__(self, titulo, autor, disponivel, emprestado_para):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel
        self.emprestado_para = emprestado_para

    def emprestar(self, pessoa):
        if self.disponivel == False:
            raise Exception("Livro já emprestado.")
        pessoa.livros_emprestados.append(self.titulo)
        self.disponivel = False
        self.emprestado_para = pessoa.nome

    def devolver(self, pessoa):
        if self.disponivel:
            raise Exception("Livro não está emprestado.")
        pessoa.livros_emprestados.remove(self.titulo)
        self.disponivel = True
        self.emprestado_para = None



    def __str__(self):
        status = "Disponível" if self.disponivel else f"Emprestado para {self.emprestado_para}" 
        return f"{self.titulo} - {self.autor} - {status}"
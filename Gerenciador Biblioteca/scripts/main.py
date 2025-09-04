from pessoas import Leitor
from menu import MenuADM, MenuLeitor
from data import carregar_dados
def main():
    livros, pessoas = carregar_dados()
    {print(p) for p in pessoas}
    while True:
        print("1. Acesso como Administrador\n2. Acesso como Leitor\n3. Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            login = input("Digite o ID do administrador: ")
            for p in pessoas:
                if p.id == login and p.admin:
                    menu_adm = MenuADM()
                    menu_adm.exibir_menu(livros, pessoas)
                    break
            else:
                print("Acesso negado. ID inválido.")


        elif opcao == "2":
            login = input("Digite o ID do leitor: ")
            for p in pessoas:
                if p.id == login:
                    menu_leitor = MenuLeitor(p.id)
                    menu_leitor.exibir_menu(livros, pessoas)
                    break
            else:
                print("Acesso negado. ID inválido.")

        elif opcao == "3":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
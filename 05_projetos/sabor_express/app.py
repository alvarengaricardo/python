'''

Treinamento em Python
Desenvolvimento de um App para restaurantes

'''

import os

restaurantes = ['Pizzaria', 'Churrascaria']


def voltar_menu():
    input('\nDigite uma tecla para voltar ao menu principal. ')
    main()


def exibir_subtitulo(texto):
    os.system('cls')
    print('\n' + texto + '\n')


def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes:')
    nome_do_restaurante = input('Digite nome do novo restaurante: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso.')
    voltar_menu()


def listar_restaurantes():
    exibir_subtitulo('Lista de Restaurantes:')
    for restaurante in restaurantes:
        print(restaurante)
    voltar_menu()


def opcao_invalida():
    print('Opção inválida!\n')
    voltar_menu()


def finalizar_app():
    exibir_subtitulo('Finalizando App\n')


def exibir_nome():
    print("""
        ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
        ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
        ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
        ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
        ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
        ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
        """)


def escolher_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restautante')
    print('4. Sair\n')

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print('Ativar restaurante')
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system('cls')
    exibir_nome()
    escolher_opcoes()


if __name__ == '__main__':
    main()

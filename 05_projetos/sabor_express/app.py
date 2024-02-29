'''

Treinamento em Python
Desenvolvimento de um App para restaurantes

'''

import os

# com listas:
# restaurantes = ['Pizzaria', 'Churrascaria']

# com dicionários
restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
                {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
                {'nome': 'Cantina', 'categoria': 'Italiana', 'ativo': False}]


def voltar_menu():
    input('\nDigite uma tecla para voltar ao menu principal. ')
    main()


def exibir_subtitulo(texto):
    os.system('cls')
    print('\n' + texto + '\n')


def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes:')
    nome_do_restaurante = input('Digite nome do novo restaurante: ')
    categoria = input(f'Categoria de {nome_do_restaurante}: ')
    dados_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso.')
    voltar_menu()


def listar_restaurantes():
    exibir_subtitulo('Lista de Restaurantes:')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo = restaurante['ativo']
        ativo = 'Ativo' if ativo else 'Não Ativo'
        print(f'- {nome_restaurante} | {categoria_restaurante} | {ativo}')
    voltar_menu()


def alternar_estado_restaurante():
    exibir_subtitulo('Alternando estado do restaurante.')
    nome_restaurante = input('Nome do restaurante para alteração de estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso.' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso.'
            print(mensagem)

    if not restaurante_encontrado:
        print(f'Restaurante {nome_restaurante} não foi encontrado.')

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
    print('3. Ativar/Desativar restautante')
    print('4. Sair\n')

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_estado_restaurante()
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

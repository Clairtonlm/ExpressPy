import os

restaurante = ['Pizza', 'Hamburguer', 'Pastel']
# lista


def exibir_nome_do_programa():
    print("""𝖲𝖺𝖻𝗈𝗋 𝖤𝗑𝗉𝗋𝖾𝗌𝗌
      
      """)
def exibir_opcoes():
    print('1- Cadastrar restaurante')
    print('2- Listar restaurantes')     
    print('3- Ativar restaurante')
    print('4- Sair')



def finalizar_app():
    os.system('clear')
    print(f'Obrigado por usar o app!\n')

def opcao_invalida():
    print('Opção inválida!\n')
    input('Pressione ENTER para voltar ao menu')
    main()

def cadastrar_restaurante():
    os.system('clear')
    print('Cadastrando restaurante\n')
    nome_do_restaurante = input('Nome do restaurante: ')
    restaurante.append(nome_do_restaurante)
    print(f'Restaurante {nome_do_restaurante} adicionado com sucesso!\n')
    input('Pressione ENTER para voltar ao menu')
    main()

def listar_restaurantes():
    os.system('clear')
    print('Listando restaurantes\n')
    print(restaurante)
    input('Pressione ENTER para voltar ao menu')
    main()

def escolher_opcao():
    try:
        opcao = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção: {opcao}')

        if opcao == 1:
            cadastrar_restaurante()
        elif opcao == 2:
            listar_restaurantes()
        elif opcao == 3:
            print('Ativando restaurante...')
        elif opcao == 4:
            finalizar_app()
        else:
            opcao_invalida()

    except ValueError:
        opcao_invalida()


# programa principal para nao ser importado
def main():
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    


if __name__ == '__main__':
    main()
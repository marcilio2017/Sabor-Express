import os

def exibir_nome_do_programa():
    print ('Sabor Express\n')

def exibir_opcoes():

    print ('1 - Cadastrar Restaurante')
    print ('2 - Listar Restaurante')
    print ('3 - Ativar Restaurante')
    print ('4 - Sair\n')

def finalizar_app():
    os.system('cls')#limpando a tela
    print('Encerrando app.\n')


opcao_escolhida = int(input('Escolha uma opção: '))
print(opcao_escolhida)

if opcao_escolhida == 1:
    print('Restaurante Cadastrado:')
elif opcao_escolhida == 2:
    print ('Listar Restaurantes:')
elif opcao_escolhida == 3:
    print ('Ativar Restaurante:')
else:
    finalizar_app()

def main():
    exibir_nome_do_programa()
    exibir_opcoes()

if __name__ == '__main__':
    main()

    




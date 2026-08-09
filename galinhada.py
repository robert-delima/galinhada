def calcular_galinhas(quantidade_galinhas, dias):
    ovos = quantidade_galinhas * dias
    racao_em_gramas = quantidade_galinhas * 126 * dias
    racao_kg = racao_em_gramas / 1000
    custo_racao = racao_kg * 2.50
    faturamento = ovos * 1.00

    lucro = faturamento - custo_racao

    print(f'Ovos: {ovos}')
    print(f'Ração: {racao_kg:.2f} kg')
    print(f'Faturamento: R$ {faturamento:.2f}')
    print(f'Custo da ração: R$ {custo_racao:.2f}')
    print(f'Resultado após ração: R$ {lucro:.2f}')

def quantas_galinhas():
    while True:
        quantidade_galinhas = int(input('Quantas Galinhas: '))

        if quantidade_galinhas <= 0:
            print('Quantidade Invalida')
        else:
            return quantidade_galinhas

def menu():
    print('='*25)
    print('     GALINHADA')
    print('='*25)
    print()
    print('1 - Gestão Diaria')
    print('2 - Gestão Semanal')
    print('3 - Gestão Mensal')
    print('4 - Gestão Vida Ùtil (100 semanas)')
    print('5 - Gestão Personalizada')
    print('6 - Sair.')
    print()

while True:
    menu()
    opcao = int(input('Opção: '))

    if opcao == 1:
        quantidade_galinhas = quantas_galinhas()

        print('-'*20)
        print('    DIARIO')
        print()
        calcular_galinhas(quantidade_galinhas, 1)
        print()
        print('-' * 20)

    elif opcao == 2:
        quantidade_galinhas = quantas_galinhas()

        print('-' * 20)
        print('    SEMANAL')
        print()
        calcular_galinhas(quantidade_galinhas, 7)
        print()
        print('-' * 20)

    elif opcao == 3:
        quantidade_galinhas = quantas_galinhas()

        print('-' * 20)
        print('    MENSAL')
        print()
        calcular_galinhas(quantidade_galinhas, 30)
        print()
        print('-' * 20)

    elif opcao == 4:
        quantidade_galinhas = quantas_galinhas()

        print('-' * 20)
        print('    VIDA UTIL')
        print()
        calcular_galinhas(quantidade_galinhas, 700)
        print()
        print('-' * 20)

    elif opcao == 5:
        quantidade_galinhas = quantas_galinhas()

        print('-' * 20)
        print('    PERSONALIZADO')
        print()
        dias_personalizado = int(input('Quantos Dias?: '))

        if dias_personalizado <= 0:
            print('Quantidade de dias inválida.')
            continue

        calcular_galinhas(quantidade_galinhas, dias_personalizado)
        print()
        print('-' * 20)

    elif opcao == 6:
        print()
        print('=' * 35)
        print('Obrigado por utilizar o programa!')
        print('Espero ter ajudado nos seus cálculos. 🐔🥚')
        print()
        print('Até breve!')
        print()
        print('Desenvolvido por Robert Souza')
        print('=' * 35)

        input('\nPressione ENTER para fechar...')
        break

    else:
        print('Operação Invalida, tente novamente')



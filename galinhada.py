import sqlite3
from datetime import date


conexao = sqlite3.connect('galinhada.db')
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS producao(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data DATE,
        quantidade_galinhas INTEGER,
        quantidade_ovos INTEGER,
        racao_kg REAL
    );
""")

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

def consultar_por_data_inicio_fim():
    data_inicial = input('Digite a data Inicial (AAAA-MM-DD): ')
    data_final = input('Digite a data Final (AAAA-MM-DD): ')

    cursor.execute("""
        SELECT SUM(quantidade_ovos), SUM(racao_kg)
        FROM producao 
        WHERE data BETWEEN ? AND ?
""", (data_inicial, data_final))

    resultado = cursor.fetchone()

    if resultado[0] is None:
        print('-' * 30)
        print()
        print('Nenhuma produção encontrada nesse período.')

    else:
        print('-'*30)
        print()
        print(f'Total de ovos no período: {resultado[0]}')
        print(f'Total de ração no período: {resultado[1]:.2f} kg')


def consultar_por_data():
    data = input('Digite a data (AAAA-MM-DD): ')

    cursor.execute("""
        SELECT *
        FROM producao
        WHERE data = ?
    """, (data,))

    dados = cursor.fetchall()

    if not dados:
        print(f'Nenhuma produção encontrada nessa data.')

    for registro in dados:
        print('='*30)
        print()
        print(f'Data: {registro[1]}')
        print(f'Galinhas: {registro[2]}')
        print(f'Ovos Produzidos: {registro[3]}')
        print(f'Ração Utilizada: {registro[4]:.2f} kg')


def total_ovos():
    cursor.execute("""
        SELECT SUM(quantidade_ovos), SUM(racao_kg)
        FROM producao
    """)

    resultado = cursor.fetchone()

    print(f'Total de ovos produzidos: {resultado[0]}')
    print(f'Total de ração utilizada: {resultado[1]:.2f} kg')


def consultar_producao():
    cursor.execute("""
        SELECT *
        FROM producao
    """)

    dados = cursor.fetchall()

    for registro in dados:
        print('-' * 30)
        print()
        print(f'ID: {registro[0]}')
        print(f'Data: {registro[1]}')
        print(f'Galinhas: {registro[2]}')
        print(f'Ovos Produzidos: {registro[3]}')
        print(f'Ração Utilizada: {registro[4]:.2f} kg')
        print()


def registrar_producao():
    quantidade_galinhas = int(input('Quantas Galinhas: '))
    quantidade_ovos = int(input('Quantos ovos: '))
    racao_utilizada = float(input('Quantos kg de ração: '))
    data = date.today().isoformat()

    cursor.execute("""
        INSERT INTO producao (data, quantidade_galinhas, 
        quantidade_ovos, racao_kg)
        VALUES (?, ?, ?, ?)
    """, (data, quantidade_galinhas, quantidade_ovos, racao_utilizada))

    conexao.commit()

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
    print('6 - Registrar Produção')
    print('7 - Consultar Produção')
    print('8 - Sair.')
    print('9 - Função Teste Soma Total')
    print('10 - Função Teste Consultar Data')
    print('11 - Função teste consultar por data determinada')
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
        registrar_producao()

    elif opcao == 7:
        consultar_producao()

    elif opcao == 8:
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
    elif opcao == 9:
        total_ovos()

    elif opcao == 10:
        consultar_por_data()

    elif opcao == 11:
        consultar_por_data_inicio_fim()

    else:
        print('Operação Invalida, tente novamente')
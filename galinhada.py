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

def deletar_producao():
    id_producao = int(input('ID da Produção: '))
    print()

    cursor.execute("""
        DELETE FROM producao
        WHERE id = ?
        """, (id_producao,))

    if cursor.rowcount == 0:
        print()
        print('Produção não encontrada')
        print()

    else:
        conexao.commit()

        print()
        print('Produção Apagada com sucesso!')
        print()

def editar_producao():
    id_producao = int(input('ID da Produção: '))
    nova_quantidade_ovos = int(input('Nova Quantidade de Ovos: '))
    print()

    cursor.execute("""
                   UPDATE producao
                   SET quantidade_ovos = ?
                   WHERE id = ?
                   """, (nova_quantidade_ovos, id_producao))

    if cursor.rowcount == 0:
        print()
        print('Produção não encontrada')
        print()

    else:
        conexao.commit()

        print()
        print('Produção atualizada com sucesso!')
        print()



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

def consultar_por_periodo():
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


def relatorio_producao():
    cursor.execute("""
        SELECT SUM(quantidade_ovos), SUM(racao_kg)
        FROM producao
    """)

    resultado = cursor.fetchone()

    print('-'*30)
    print()
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

    try:
        cursor.execute("""
            INSERT INTO producao (data, quantidade_galinhas, 
            quantidade_ovos, racao_kg)
            VALUES (?, ?, ?, ?)
        """, (data, quantidade_galinhas, quantidade_ovos, racao_utilizada))

        conexao.commit()

        print()
        print('Registro Concluido com Sucesso!')
        print()

    except sqlite3.Error as erro:
        print()
        print(f'Erro ao registrar produção: {erro}')
        print()

def quantas_galinhas():
    while True:
        quantidade_galinhas = int(input('Quantas Galinhas: '))

        if quantidade_galinhas <= 0:
            print('Quantidade Invalida')
        else:
            return quantidade_galinhas

def menu_calculadora():
    while True:
        print('===== CALCULADORA DE PROJEÇÃO =====')
        print()
        print('1 - Diario')
        print('2 - Semanal')
        print('3 - Mensal')
        print('4 - Vida Útil')
        print('5 - Personalizado')
        print('6 - Voltar')

        opcao_calculadora = int(input('Opção: '))

        if opcao_calculadora == 1:
            quantidade_galinhas = quantas_galinhas()

            print('-' * 20)
            print('    DIARIO')
            print()
            calcular_galinhas(quantidade_galinhas, 1)
            print()
            print('-' * 20)

        elif opcao_calculadora == 2:
            quantidade_galinhas = quantas_galinhas()

            print('-' * 20)
            print('    SEMANAL')
            print()
            calcular_galinhas(quantidade_galinhas, 7)
            print()
            print('-' * 20)

        elif opcao_calculadora == 3:
            quantidade_galinhas = quantas_galinhas()

            print('-' * 20)
            print('    MENSAL')
            print()
            calcular_galinhas(quantidade_galinhas, 30)
            print()
            print('-' * 20)

        elif opcao_calculadora == 4:
            quantidade_galinhas = quantas_galinhas()

            print('-' * 20)
            print('    VIDA UTIL')
            print()
            calcular_galinhas(quantidade_galinhas, 700)
            print()
            print('-' * 20)

        elif opcao_calculadora == 5:
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

        elif opcao_calculadora == 6:
            break

def menu():
    print('='*25)
    print('     GALINHADA')
    print('='*25)
    print()
    print('1 - Registrar Produção')
    print('2 - Consultar Produção')
    print('3 - Consultar Produção por Data')
    print('4 - Consultar Produção por Período')
    print('5 - Relatório de Produção')
    print('6 - Editar Produção')
    print('7 - Excluir Produção')
    print('8 - Calculadora de Projeção')
    print('9 - Sair')
    print()

while True:
    menu()
    opcao = int(input('Opção: '))

    if opcao == 1:
        registrar_producao()

    elif opcao == 2:
        consultar_producao()

    elif opcao == 3:
        consultar_por_data()

    elif opcao == 4:
        consultar_por_periodo()

    elif opcao == 5:
        relatorio_producao()

    elif opcao == 6:
        editar_producao()

    elif opcao == 7:
        deletar_producao()

    elif opcao == 8:
        menu_calculadora()

    elif opcao == 9:
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
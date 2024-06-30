menu = '''-------------------------
[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Sair
-------------------------
Nº da operação: '''
saldo = 0
saques_feitos_hoje = 0
limite_saques_diarios = 3
operacoes = []
numero_operacao = 1

def operacao():
    op = input(menu)
    return op

def sacar(valor):
    global saldo, saques_feitos_hoje, operacoes, numero_operacao
    
    if saques_feitos_hoje >= limite_saques_diarios:
        print('Você já realizou o máximo de 3 saques diários.')
    elif valor > saldo:
        print('Sua tentativa de saque é maior que seu saldo.')
    elif valor > 500:
        print('O limite do valor de saque por operação é de R$500.')
    else:
        saldo -= valor
        saques_feitos_hoje += 1
        operacoes.append(f'{numero_operacao} - Saque: R${valor:.2f}')
        numero_operacao += 1
        print(f'Você sacou R${valor:.2f} com sucesso.')

    return

def depositar(valor):
    global saldo, operacoes, numero_operacao

    saldo += valor
    operacoes.append(f'{numero_operacao} - Depósito: R${valor:.2f}')
    numero_operacao += 1
    print(f'Você depositou R${valor:.2f} com sucesso.')

    return

def extrato():
    global saldo, operacoes
    
    print('\nEXTRATO BANCÁRIO')
    if operacoes:
        for operacao in operacoes:
            print(operacao)
    else:
        print('Nenhuma operação realizada.')
    print(f'\nSaldo atual: R${saldo:.2f}')

    return

def continuar_sair():
    escolha = input("\nDigite 's' para continuar ou 'n' para sair do sistema: ")
    while escolha.lower() not in ['s', 'n']:
        escolha = input("Escolha inválida. Digite 's' para continuar ou 'n' para sair do sistema: ")
    if escolha.lower() == 'n':
        print('Saindo do sistema.')
        exit()

while True:
    opcao = operacao()

    if opcao == '1':
        valor = float(input('\nValor do depósito: '))
        depositar(valor)
        continuar_sair()

    elif opcao == '2':
        valor = float(input('\nValor do saque: '))
        sacar(valor)
        continuar_sair()

    elif opcao == '3':
        extrato()
        continuar_sair()

    elif opcao == '4':
        print('\nSaindo do sistema.')
        break

    else:
        print('\nOperação inválida, digite um número de 1 a 4.')

Menu = '''
1 - Depositar

2 - Sacar

3 - Extrato

4 - Sair

'''
def main(Menu):
    Saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = input(Menu)
        
        if opcao == '1':
            valor = float(input('Informe o valor do deposito: '))
            if valor > 0:
                Saldo += valor
                extrato += f'Deposito: R$ {valor:.2f}\n'
            else:
                print('Operação falhou! O valor informado é inválido.')
        elif opcao == '2':
            
            valor = float(input('Informe o valor do Saque: '))
            
            excedeu_saldo = valor > Saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES
            
            
            if excedeu_saldo:
                print('Olá pobre imunda(o), você não tem dinheiro a mais na conta.')
            elif excedeu_limite:
                print('Passou do limite dog, não vai receber nada.')
            elif excedeu_saques:
                print('Já foi o número máximo de saques.')
            elif valor > 0:
                Saldo -= valor
                extrato +=  f'Saque: R${valor:.2f}\n'
                numero_saques += 1
            else:
                print('Faltou ação')
                
        elif opcao == '3':
            print('Não foram realizadas nenhuma movimentação.' if not extrato else extrato)
            print(f'\nSaldo:{Saldo:.2f}R$')
        elif opcao == '4':
            print('É isso tmj')
            break
        else:
            print('Escolhe ai de 1 a 4 de novo')
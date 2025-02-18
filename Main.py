import textwrap
def menu():
    menu = '''
    1 - Depositar

    2 - Sacar

    3 - Extrato

    nc - Nova Conta

    lc - Listar Contas

    nu - Novo Usuário

    4 - Sair

    '''
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Deposito: R$ {valor:.2f}\n'
        print('Operação realizada com sucesso!')
    else:
        print('Operação falhou! O valor informado é inválido.')
    return saldo, extrato

def sacar(*, saldo, valor, limite, extrato, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    if excedeu_saldo:
        print('Olá pobre imunda(o), você não tem dinheiro a mais na conta.')
    elif excedeu_limite:
        print('Passou do limite dog, não vai receber nada.')
    elif excedeu_saques:
        print('Já foi o número.máximo de saques.')
    elif valor > 0:
        saldo -= valor
        extrato +=  f'Saque: R${valor:.2f}\n'
        numero_saques += 1
        print('Operação realizada com sucesso!')
    else:
        print('Faltou ação')
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print('Extrato:')
    print('Não foram realizadas movimentações'if not extrato else extrato)
    print(f'\nSaldo:{saldo:.2f}R$')

def criar_usuario(usuarios):
    cpf = input('Informe o CPF (somente numeros): ')
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print('Ja existe um usuario com esse CPF')
        return
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereço = input('Informe o endereço: ')
    
    usuarios.append({
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereço})
    print('Usuario criado com sucesso!')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuario: ')
    usuario = filtrar_usuario(cpf,usuarios)
    
    if usuario:
        print('Conta criada com sucesso!')
        return {
            'agencia': agencia,
            'numero': numero_conta,
            'usuario': usuario}
    print('Usuario não encontrado!')

def listar_contas(contas):
    for conta in contas:
        print(f'Agência: {conta["agencia"]}')
        print(f'Número: {conta["numero_conta"]}')
        print(f'TItular: {conta["usuario"]["nome"]}')
    else:
        print('Nenhuma conta cadastrada')
def main():
    AGENCIA = '0001'
    LIMITE_SAQUES = 3
    
    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        
        if opcao == '1':
            valor = float(input('Informe o valor do deposito: '))
            
            saldo, extrato = depositar(saldo, valor, extrato)
            
        elif opcao == '2':
            valor = float(input('Informe o valor do Saque: '))
            
            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                limite = limite,
                extrato = extrato,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )

        elif opcao == '3':
            exibir_extrato(saldo, extrato = extrato)

        elif opcao == 'nu':
            criar_usuario(usuarios)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == 'lc':
            listar_contas(contas)
            
        elif opcao == '4':
            print('É isso tmj')
            break

        else:
            print('Escolhe ai de 1 a 4 de novo')
main()
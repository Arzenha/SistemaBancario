from abc import ABC, abstractmethod
from datetime import datetime
import textwrap

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
        
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo
        if excedeu_saldo:
            print('Saldo insuficiente')
        elif valor > 0:
            self._saldo -= valor
            print('Saque realizado com sucesso')
            return True
        else:
            print('Operação falhou! O valor informado é inválido.')
        return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print('Depósito realizado')
        else:
            print('Operação falhou! O valor informado é inválido.')
            return False
        
        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
    
    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao['tipo']== Saque.__name__]
        )
        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print('Limite excedido')
        elif excedeu_saques:
            print('Limite de saques excedido')
        
        else:
            return super().sacar(valor)

        return False
    
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

class Historico:
    def __init__(self):
        self.transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self.transacoes.append(
            {
                'tipo': transacao.__class__.__name__,
                'valor': transacao.valor,
                'data': datetime.now().strftime('%d-%m-%Y %H:%M:%S'),
            }
        )

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass
    
    @classmethod
    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

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
    return input((menu))

def depositar(usuarios):
    cpf = input('Informe o CPF do Cliente: ')
    usuario = filtrar_usuario(cpf, usuarios)
    
    if not usuario:
        print('Cliente nao encontrado')
        return
    
    valor = float(input('Informe o valor do depósito: '))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(usuario)
    if not conta:
        return

    usuario.realizar_transacao(conta, transacao)

def sacar(usuarios):
    cpf = input('Informe o CPF do cliente: ')
    usuario = filtrar_usuario(cpf, usuarios)
    
    if not usuario:
        print('Cliente nao encontrado')
        return
    
    valor = float(input('Informe o valor do saque: '))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(usuario)
    if not conta:
        return

    usuario.realizar_transacao(conta, transacao)

def exibir_extrato(usuarios):
    cpf = input('Informe o CPF do cliente: ')
    usuario = filtrar_usuario(cpf, usuarios)
    
    if not usuario:
        print('Cliente nao encontrado')
        return
    
    conta = recuperar_conta_cliente(usuario)
    if not conta:
        return

    print(f'Extrato da conta {conta.numero}')
    transacoes = conta.historico.transacoes
    
    extrato = ''
    if not transacoes:
        extrato = 'Nenhuma transação realizada'
    else:
        for transacao in transacoes:
            extrato += f'{transacao["data"]} - {transacao["tipo"]} - {transacao["valor"]}\n'

    print(extrato)
    print(f'Saldo atual: {conta.saldo:.2f}')

def criar_usuario(usuarios):
    cpf = input('Informe o CPF (somente numeros): ')
    # Filtrar usuarios
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print('Ja existe um usuario com esse CPF')
        return
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereço = input('Informe o endereço: ')

    usuario = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereço=endereço)

    usuarios.append(usuario)
    print('Cliente criado com sucesso!')

def filtrar_usuario(cpf, usuarios):
    # Se tiver um usuario com o cpf informado, retorna o usuario
    usuarios_filtrados = [usuario for usuario in usuarios if usuario.cpf == cpf]
    # retorna o primeiro usuario da lista de usuarios filtrados, se não tiver nenhum retorna None
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(contas, numero_conta, usuarios):
    cpf = input('Informe o CPF do Cliente: ')
    usuario = filtrar_usuario(cpf,usuarios)

    if not usuario:
        print('Cliente não encontrado')
        return

    conta = ContaCorrente.nova_conta(usuario=usuario, numero=numero_conta)
    contas.append(conta)
    usuario.contas.append(conta)
    print('Conta criada com sucesso!')

def listar_contas(contas):
    # Percorrer a lista de contas
    for conta in contas:
        print(textwrap.dedent(str(conta)))

def recuperar_conta_cliente(usuarios):
    if not usuarios.contas:
        print('Cliente não possui contas')
        return 

        # FIXME: Cliente não permite acessar contas diretamente
        return usuarios.contas[0]

def main():
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == '1':
            depositar(usuarios)

        elif opcao == '2':
            sacar(usuarios)

        elif opcao == '3':
            exibir_extrato(usuarios)

        elif opcao == 'nu':
            criar_usuario(usuarios)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, usuarios, contas)

        elif opcao == 'lc':
            listar_contas(contas)
            
        elif opcao == '4':
            print('É isso tmj')
            break

        else:
            print('Escolhe ai de 1 a 4 de novo')

main()
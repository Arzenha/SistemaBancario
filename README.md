Sistema Bancário com Flet
Este projeto é um sistema bancário simples desenvolvido com a biblioteca Flet para interface gráfica e Python para lógica de negócios. Ele permite realizar operações como Depósito, Saque e Exibição de Extrato de contas bancárias.

Estrutura do Projeto
A estrutura do projeto está organizada da seguinte forma:

SistemaBancario/
├── Sistem/
│   ├── PrincipalPG.py
│   ├── Main.py
├── README.md

Descrição dos Arquivos
1. PrincipalPG.py
    Este é o arquivo principal que contém a interface gráfica do sistema bancário. Ele utiliza a biblioteca Flet para criar uma interface amigável e interativa.

Funcionalidades:

Depósito: Permite realizar depósitos em contas bancárias.
Saque: Permite realizar saques de contas bancárias.
Extrato: Exibe o histórico de transações de uma conta bancária.
Navegação: Inclui uma barra de navegação com ícones para diferentes seções.
Componentes Importantes:

Botões:
    Botão de Depósito: Azul com ícone de pagamento.
    Botão de Saque: Azul com ícone de caixa eletrônico.
    Botão de Extrato: Azul com ícone de recibo.
Diálogos:
    Exibe mensagens de erro ou sucesso ao realizar operações.
Barra de Navegação:
    Ícones para "Perfil", "Segurança" e "Configurações".
2. Main.py
    Este arquivo contém a lógica de negócios do sistema bancário. Ele define as classes e funções necessárias para gerenciar contas bancárias e realizar transações.

Funcionalidades:
    Classes:
        ContaCorrente: Representa uma conta bancária.
        Transacao: Classe base para transações.
        Deposito e Saque: Subclasses de Transacao para operações específicas.
Funções:
    filtrar_usuario: Filtra usuários com base no CPF.
    recuperar_conta_cliente: Recupera a conta de um cliente.

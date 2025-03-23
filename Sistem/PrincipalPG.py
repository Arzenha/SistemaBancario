import flet as ft
from Main import Saque, Deposito, filtrar_usuario, recuperar_conta_cliente

# Função principal do Flet
def main(page: ft.Page):
    page.title = 'Sistema Bancário'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.height = 640
    page.window.width = 360
    page.bgcolor = 'white'
    page.scroll = "adaptive"

    # Lista de usuários e contas (simulação de banco de dados)
    usuarios = []
    contas = []

    # Função para realizar depósito
    def realizar_deposito(e):
        def confirmar(e):
            cpf = cpf_input.value.strip()
            valor = valor_input.value.strip()

            if not cpf or not valor:
                page.dialog = ft.AlertDialog(title=ft.Text("Preencha todos os campos!"))
                page.dialog.open = True
                page.update()
                return

            try:
                valor = float(valor)
            except ValueError:
                page.dialog = ft.AlertDialog(title=ft.Text("Valor inválido!"))
                page.dialog.open = True
                page.update()
                return

            usuario = filtrar_usuario(cpf, usuarios)

            if not usuario:
                page.dialog = ft.AlertDialog(title=ft.Text("Usuário não encontrado!"))
                page.dialog.open = True
                page.update()
                return

            conta = recuperar_conta_cliente(usuario)
            if not conta:
                page.dialog = ft.AlertDialog(title=ft.Text("Usuário não possui conta!"))
                page.dialog.open = True
                page.update()
                return

            transacao = Deposito(valor)
            transacao.registrar(conta)
            page.dialog = ft.AlertDialog(title=ft.Text("Depósito realizado com sucesso!"))
            page.dialog.open = True
            page.update()

        cpf_input = ft.TextField(label="CPF do Cliente")
        valor_input = ft.TextField(label="Valor do Depósito", keyboard_type="number")
        confirmar_button = ft.ElevatedButton("Confirmar", on_click=confirmar)

        page.dialog = ft.AlertDialog(
            title=ft.Text("Realizar Depósito"),
            content=ft.Column([cpf_input, valor_input, confirmar_button]),
        )
        page.dialog.open = True
        page.update()

    # Função para realizar saque
    def realizar_saque(e):
        def confirmar(e):
            cpf = cpf_input.value.strip()
            valor = valor_input.value.strip()

            if not cpf or not valor:
                page.dialog = ft.AlertDialog(title=ft.Text("Preencha todos os campos!"))
                page.dialog.open = True
                page.update()
                return

            try:
                valor = float(valor)
            except ValueError:
                page.dialog = ft.AlertDialog(title=ft.Text("Valor inválido!"))
                page.dialog.open = True
                page.update()
                return

            usuario = filtrar_usuario(cpf, usuarios)

            if not usuario:
                page.dialog = ft.AlertDialog(title=ft.Text("Usuário não encontrado!"))
                page.dialog.open = True
                page.update()
                return

            conta = recuperar_conta_cliente(usuario)
            if not conta:
                page.dialog = ft.AlertDialog(title=ft.Text("Usuário não possui conta!"))
                page.dialog.open = True
                page.update()
                return

            transacao = Saque(valor)
            transacao.registrar(conta)
            page.dialog = ft.AlertDialog(title=ft.Text("Saque realizado com sucesso!"))
            page.dialog.open = True
            page.update()

        cpf_input = ft.TextField(label="CPF do Cliente")
        valor_input = ft.TextField(label="Valor do Saque", keyboard_type="number")
        confirmar_button = ft.ElevatedButton("Confirmar", on_click=confirmar)

        page.dialog = ft.AlertDialog(
            title=ft.Text("Realizar Saque"),
            content=ft.Column([cpf_input, valor_input, confirmar_button]),
        )
        page.dialog.open = True
        page.update()

    # Função para exibir extrato
    def exibir_extrato(e):
        def confirmar(e):
            cpf = cpf_input.value.strip()
            usuario = filtrar_usuario(cpf, usuarios)

            if not usuario:
                page.dialog = ft.AlertDialog(title=ft.Text("Usuário não encontrado!"))
                page.dialog.open = True
                page.update()
                return

            conta = recuperar_conta_cliente(usuario)
            if not conta:
                page.dialog = ft.AlertDialog(title=ft.Text("Usuário não possui conta!"))
                page.dialog.open = True
                page.update()
                return

            transacoes = conta.historico.transacoes
            extrato = "\n".join(
                [f"{t['data']} - {t['tipo']} - R$ {t['valor']:.2f}" for t in transacoes]
            )
            page.dialog = ft.AlertDialog(
                title=ft.Text("Extrato da Conta"),
                content=ft.Text(extrato if extrato else "Nenhuma transação realizada."),
            )
            page.dialog.open = True
            page.update()

        cpf_input = ft.TextField(label="CPF do Cliente")
        confirmar_button = ft.ElevatedButton("Confirmar", on_click=confirmar)

        page.dialog = ft.AlertDialog(
            title=ft.Text("Exibir Extrato"),
            content=ft.Column([cpf_input, confirmar_button]),
        )
        page.dialog.open = True
        page.update()

    # Botões de ação com melhorias
    deposito_button = ft.ElevatedButton(
        "Depósito",
        icon=ft.icons.PAYMENTS,
        bgcolor=ft.colors.BLUE_400,
        color=ft.colors.WHITE,
        on_click=realizar_deposito,
    )
    saque_button = ft.ElevatedButton(
        "Saque",
        icon=ft.icons.ATM,
        bgcolor=ft.colors.BLUE_400,
        color=ft.colors.WHITE,
        on_click=realizar_saque,
    )
    extrato_button = ft.ElevatedButton(
        "Extrato",
        icon=ft.icons.RECEIPT_LONG,
        bgcolor=ft.colors.BLUE_400,
        color=ft.colors.WHITE,
        on_click=exibir_extrato,
    )

    # Layout principal com espaçamento
    page.add(
        ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text("Conta Bancária", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE),
                ),
                ft.Container(
                    height=50,
                    width=300,
                    content=deposito_button, 
                    margin=ft.margin.only(top=10)
                ),
                ft.Container(
                    height=50,
                    width=300,
                    content=saque_button, 
                    margin=ft.margin.only(top=10)
                ),
                ft.Container(
                    height=50,
                    width=300,
                    content=extrato_button, 
                    margin=ft.margin.only(top=10)
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=ft.CrossAxisAlignment.START,
        )
        
    ),
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.PERSON, label=""),
            ft.NavigationDestination(icon=ft.icons.SECURITY, label=""),
            ft.NavigationDestination(icon=ft.icons.SETTINGS, label=""),]
    )
    page.update()

ft.app(main)
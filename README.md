# Sistema Bancário com Flet

Este projeto implementa uma interface bancária utilizando a biblioteca [Flet](https://flet.dev/), permitindo realizar operações como depósito, saque e consulta de extrato.

## Funcionalidades
- **Depósito**: Permite ao usuário inserir o CPF e o valor a ser depositado.
- **Saque**: Permite ao usuário inserir o CPF e o valor a ser sacado.
- **Exibir Extrato**: Mostra o histórico de transações de um cliente.

## Tecnologias Utilizadas
- **Python**
- **Flet** (para a interface gráfica)

## Como Executar

1. Instale as dependências necessárias:
   ```sh
   pip install flet
   ```
2. Execute o script principal:
   ```sh
   python PrincipalPG.py
   ```

## Estrutura do Projeto

```
/
|-- PrincipalPG.py  # Script principal com a interface
|-- Main.py         # Contém as classes e funções de Saque, Depósito, etc.
```

## Como Funciona

1. O sistema apresenta uma tela com três opções: **Depósito**, **Saque** e **Extrato**.
2. Ao selecionar uma opção, um formulário aparece solicitando o CPF do cliente e o valor da operação.
3. O sistema valida os dados e processa a transação.
4. Se bem-sucedida, a operação é registrada e o saldo atualizado.
5. O histórico de transações pode ser consultado na opção **Extrato**.

## Possíveis Melhorias
- Persistência de dados (atualmente os dados são perdidos ao fechar o programa)
- Implementação de um banco de dados
- Autenticação de usuários

## Autor
Desenvolvido para fins educacionais e aprendizado de Flet.

---

Sinta-se à vontade para modificar e melhorar o projeto!



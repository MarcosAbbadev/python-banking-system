def l():
    print("==" * 25)


def line(msg):
    l()
    print(msg)
    l()


def ler_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("\033[31mDigite um número válido.\033[0m")


def ler_int(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("\033[31mDigite um número inteiro válido.\033[0m")


saldo = 0.0

l()
print("Bem-vindo ao sistema bancário!")

while True:

    line("Escolha uma opção:\n1 - Depositar 💹\n2 - Sacar 💰\n3 - Consultar Saldo 💲\n4 - Sair 🔚")
    option = ler_int("Opção: ")
    l()

    if option == 1:
        valor_deposito = ler_float("Digite o valor a ser depositado: R$ ")
        l()

        if valor_deposito <= 0:
            print("O valor do depósito deve ser positivo.")
        else:
            saldo += valor_deposito
            print(f"💹\033[32mDepósito de R$ {valor_deposito:.2f} realizado com sucesso.\033[0m")

        
    elif option == 2:
        valor_saque = ler_float("Digite o valor a ser sacado: R$ ")
        l()

        if valor_saque <= 0:
            print("O valor do saque deve ser positivo.")
        elif valor_saque > saldo:
            print("Saldo insuficiente.")
        else:
            saldo -= valor_saque
            print(f"💰\033[33mSaque de R$ {valor_saque:.2f} realizado com sucesso.\033[0m")


    elif option == 3:
        print(f"💲Seu saldo atual é: R$ \033[32m{saldo:.2f}\033[0m")

    elif option == 4:
        print("🔚 Obrigado por usar o sistema bancário. Até logo!")
        l()
        break

    else:
        print("\033[31mOpção inválida. Tente novamente.\033[0m")

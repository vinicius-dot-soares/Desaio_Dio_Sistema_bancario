menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 1540
limite = 500
extrato = ""
numero_saques= 0
LIMITE_SAQUE = 3

while True:
     opcao = input(menu)

     if opcao == "1":
        valor = float(input("informe o valor do depósito"))
        if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}"
        else:
            print("Operação falhou! O valor informado é invalido")

     elif opcao == "2":
        valor = float(input("Informe o valor do saque"))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques =numero_saques >= LIMITE_SAQUE

        if excedeu_saldo:
                print("operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
                print("Operação falhou! Números de saques excedido.")
        elif valor > 0:
                saldo -= valor 
                extrato += f"Saque:  R${valor:.2f}\n"
                numero_saques += 1
        else:
                print("Operação falhou! O valor informado é inválido.")

     elif opcao == "3":
        print("\n============ EXTRATO ===========")
        print(extrato if extrato else "não foram realizados movimentações.")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("====================================")
        print("== Obrigado por usar nosso sistema==")


     elif opcao == "0":
        break

     else:
        print("Operação Inválida, por favor selecionar novamente a opção desejada.")           

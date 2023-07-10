menu = """ 
###  Banco  ###

1. Depositar
2. Sacar
3. extrato
4. Sair
"""
saldo = 0
limite = 500
extrato = "##  Extrato  ##"
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    print(opcao)

    match opcao:
        case 1:
            deposito = input("Qual a quantia que deseja depositar?")
            saldo += deposito
            extrato.join(f"Depósito: R${deposito}")

        case 2:
            saque = input("Qual a quantia que deseja sacar?")
            if(numero_saques > LIMITE_SAQUES): 
                print("Você excedeu o limite de saques diários")
            else:
                if(saque <= limite):
                    saldo -= saque
                    numero_saques += 1
                    print("Saque realizado com sucesso")
                elif (saque > limite):
                    print("O saque solicitado é maior do que o limite permitido para saques")
        case 3:
            print(extrato)

        case 4:
            print("Saindo!")
            break
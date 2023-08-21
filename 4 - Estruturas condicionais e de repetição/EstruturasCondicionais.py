"""If, Else, Elif"""
opcao = int(input("[1] Saque \n[2] Extrato\nDigite a opçao: "))
saldo = 2000
saque = 200

if(opcao == 1):
    saque = float(input("Digite o valor de saque: "))
    if(saque <= saldo):
        novoSaldo = saldo - saque
        print(f"Saque permitido, seu saldo atual é {novoSaldo}")
    else:
        print("Saldo indisponível")

elif(opcao == 2):
    print(f"Saldo atual: {saldo}")

else:
    print("Opção indisponível")

"""Ternário"""
'''retorno caso verdadeiro / condiçao / retorno caso falso'''
status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar saque")

"""Declarando funções"""

def exibir_mensagem():
    print("Olá mundo")

def exibir_mensagem2(nome):
    print(f"Seja bem-vindo {nome}")

def exibir_mensagem3(nome = "Anônimo"):
    print(f"Seja bem-vindo {nome}")

def calcular_total(numeros):
    return sum(numeros)

def antecessor_sucessor(numero):
    antecessor = numero-1 
    sucessor = numero+1 
    return antecessor, sucessor

"""args são tuplas e kwargs são dicionários"""
def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)


"""Chamada de funções"""
exibir_mensagem()
exibir_mensagem2(nome="Nathan") #Argumento nomeado, modele Key Value
exibir_mensagem2("Marcelo")
exibir_mensagem3()
exibir_mensagem3(nome="Chappie")

print(calcular_total([10, 23, 43, 12]))
print(antecessor_sucessor(20))

exibir_poema("Zen of Python", "Beautiful is better than ugly.", autor="Tim Peters", ano=1999)

"""Funções especiais"""
"""Tudo antes da declaração da barra é obigatório ser passado somente por posição, já após a barra pode escolher se passado por posição ou chave/valor"""
def criar_carro(modelo, ano, placa, /, marca, motor, combustível):
    print(f"1 - {modelo, ano, placa, marca, motor, combustível}")

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustível="Gasolina")

"""Aceita somente parâmetros nomeados"""
def criar_carro2(*, modelo, ano, placa, marca, motor, combustível):
    print(f"2 - {modelo, ano, placa, marca, motor, combustível}")

criar_carro2(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustível="Gasolina")

"""Objetos de primeira classe"""
def somar(a, b):
    return a+b

def exibir_resultado(a, b, func):
    resultado = func(a, b)
    print(f"\nA soma entre {a} e {b} resulta em {resultado}")

exibir_resultado(10, 10, somar)

"""escopos global e local"""
salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

print(f"\n{salario_bonus(500)}")

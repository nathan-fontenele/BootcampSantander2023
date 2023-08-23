"""Conjunto ordenado Key, Value"""
"""Chave é um valor imultável"""

pessoa1 = {"Nome": "Nathan", "Idade": 23}

pessoa = dict(Nome="Maria", Idade=28)

#-------------------------------------------
"""
for chave in pessoa:
    print(chave, pessoa["Nome"])

print()

for chave, valor in pessoa.items():
    print(chave, valor)
"""
#------------------------------------------

#pessoa.clear()
copia = pessoa.copy()
pessoa.fromkeys(["Endereço", "Cep", "Email", "Telefone"], "Vazio") #Adiciona novas chaves

for chave, valor in pessoa.items():
    print(chave, valor)






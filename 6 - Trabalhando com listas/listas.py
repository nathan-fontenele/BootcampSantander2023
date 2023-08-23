nomes = ["Nathan", "Amanda", "Jorge", "Matheus" ]
numeros = [3, 45, 74, 23, 53, 42, 65, 342, 13, 25]

print(nomes)

nomes.append("Maria") #Adiciona itens ao fim da lista

print(nomes)

nomes.pop() # Remove o útimo elemento

print(nomes)

print(nomes[1]) #Acessa um elemento

print(nomes[-1])

for i in nomes:
    letra = i
    print(letra, end=" ")

print("")

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz)

matriz.append([10, 11, 12])

print(matriz)

print(matriz[2][1])

pares = [numero for numero in numeros if numero % 2 == 0]
print(numeros)
print(pares)
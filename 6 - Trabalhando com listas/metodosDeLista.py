lista = []

lista.append("Java")
lista.append("Python")
lista.append("C")

print(lista)

#lista.pop()

print(lista.count("Python"))
#lista.clear()

lista.reverse()
print(lista)

lista.sort(key=lambda x: len(x))
print(lista)

lista.append([54, 65, 34])

lista.remove("Python")

print(lista)
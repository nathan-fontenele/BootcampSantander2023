"""Coleção de objetos de elementos únicos"""

conj = set([1, 2, 3, 3, 1, 5])
conjA = {1, 2, 3}
conjB = {4, 2, 1}

linguagens = {"python", "java", "c#", "javascript", "python"}

conj.add(6)
print(conj)
print(linguagens)

linguagens = list(linguagens)

print(linguagens[0])

conju_Union = conjA.union(conjB)

print(conju_Union)

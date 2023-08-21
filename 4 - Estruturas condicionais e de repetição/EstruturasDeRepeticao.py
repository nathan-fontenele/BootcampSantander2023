"""
texto = input("Informe um texto: ")
vogais = "AEIOU"

for letras in texto:
    if letras.upper() in vogais:
        print(letras, end="")

print()

for num in range(1, 11, 2):
    print(num, end=" ")

"""
num = 1
while num <= 100:
    if (num % 2 == 0):
        print(num, end=" ")
    num += 1

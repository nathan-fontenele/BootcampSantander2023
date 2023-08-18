print("INT -> FLOAT")
priceINT = 10

print(f"{priceINT}/2 = {priceINT/2}")
print(f"{priceINT}/2 = {priceINT//2}")

priceINT = float(priceINT)
print(f"{priceINT}")

print("\n---------------------------------------------------------------------")
print("FLOAT -> INT")
priceFLOAT = 10.30

priceFLOAT = int(priceFLOAT)
print(f"{priceFLOAT}")

print("\n---------------------------------------------------------------------")
print("INT -> STR")
priceFLOAT = 10.50
age = 28

print(str(priceFLOAT))
print(str(age))

text = f"Idade {age} preço {priceFLOAT}"
print(text)

print("\n---------------------------------------------------------------------")
print("STR -> INT e FLOAT")
priceSTR = "10.50"
ageSTR = "29"

print(float(priceSTR))
print(int(ageSTR))

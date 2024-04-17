a = float(input("Введіть розмір листа жерсті (a): "))

b = float(input("Введіть висоту коробки (b): "))

c = float(input("Введіть масу 1 см² жерсті (c): "))

S = a * a

V = S * b

M_korobky = V * c

print(f"Маса коробки: {M_korobky} г")
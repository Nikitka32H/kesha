chislo = int(input("номер квитка:"))

dig1 = chislo // 100
chislo = chislo - dig1 * 100
dig2 = chislo // 10
dig3=chislo - dig2 * 10
q = dig1 + dig2 + dig3
print("вартість квитка-",q)
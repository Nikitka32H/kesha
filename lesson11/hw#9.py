slovo=input("enter slovo")
lettern=input("enter letter")
count=0
for letter in slovo:
    if letter == lettern:
        count += 1
print(f"kilkist bukv v slove {slovo}:{count}")
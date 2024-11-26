import random

numero1 = random.randint(1,10)
print(numero1)

numero2 = random.randint(1,10)
print(numero2)

if numero1 < numero2:
    print(numero1, "è minore di", numero2)
if numero1 > numero2:
    print(numero1, "è maggiore di", numero2)
if numero1 == numero2:
    print("i due numeri sono uguali")

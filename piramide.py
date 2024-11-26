print("creerò una piramide")
h = int (input("dimmi l'altezza della piramide: "))

for i in range (1, h + 1): 
    spazi = " " * (h - i) #spazi a sinistra per centrare gli asterischi in modo tale da creare la piramide
    stelle = "*" * (2 * i - 1) #asterischi che crescono man mano che i aumenta
    print(spazi + stelle) #stampa piramide
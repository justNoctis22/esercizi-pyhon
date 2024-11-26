nome = input ("Ciao, come ti chiami? ")
print("Ciao", nome +"!")
umore = input("ti va di descrivermi tramite una scala da 1 a 10 il tuo umore? (1 significa che stai molto male e 10 significa che stai benissimo) rispondi con si o no per favore ")
if umore == "si":
    val1 = int (input("esprimi il tuo umore utilizzando la scala indicata in precedenza ")) #inserimento valore per indicare l'umore
    if val1 <= 3:
        print("mi dispiace tanto che ti senti così, ti consiglio di fare qualcosa che ti faccia liberare la mente")
    if 4 <= val1 <= 6:
        print("i giorni no ci sono per tutti, andrà bene, credo in te")
    if 7 <= val1 <= 10:
        print("sono molto felice per te! approfittane per fare qualcosa di produttivo")
elif umore == "no":
    print("capisco e accetto la tua decisione, ti auguro una buona giornata!")
else:
    print("errore: inserimento non valido")  
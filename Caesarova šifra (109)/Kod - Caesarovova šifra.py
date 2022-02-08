vstup = "ahoj"
vystup = " "

def sifra(vstup, vystup):
    for i in range(len(vstup)):
        ave = vstup[i]
        vystup+= chr(ord(ave))
    return(vystup)

sifra(vstup, vystup)
print(vystup)

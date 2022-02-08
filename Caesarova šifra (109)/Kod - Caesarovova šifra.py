vstup = "dhoj"
vystup = ""

def sifra(vstup, vystup):
    for i in range(len(vstup)):
        ave = vstup[i]
        vystup+= chr(ord(ave)+3)
    return(vystup)

sifra(vstup, vystup)
print(vystup)

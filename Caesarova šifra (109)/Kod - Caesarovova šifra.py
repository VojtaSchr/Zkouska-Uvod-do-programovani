vstup = "ahoj"
vystup = "Výstup: "
posun = 3

def sifra(input, exitus, trabea):
    for i in range(len(input)):
        ave = input[i]
        exitus += chr((ord(ave)+ trabea - 97) %26 + 97)
    return exitus

#sifra(vstup, vystup, posun)
print(sifra(vstup, vystup, posun))

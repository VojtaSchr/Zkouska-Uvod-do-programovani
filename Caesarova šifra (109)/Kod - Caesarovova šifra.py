vstup = "ahojz KYč :)"
vystup = "Výstup: "
posun = 3

print(ord("a"))
print(ord("A"))

def sifra(input, exitus, trabea):
    for i in range(len(input)):
        ave = input[i]
        if 97<=ord(ave)<=122:
            exitus += chr((ord(ave)+ trabea - 97) %26 + 97)
        elif 65<=ord(ave)<=90:
            exitus += chr((ord(ave)+ trabea - 65) %26 + 65)
        else:
            exitus += ave
    return exitus

#sifra(vstup, vystup, posun)
print(sifra(vstup, vystup, posun))

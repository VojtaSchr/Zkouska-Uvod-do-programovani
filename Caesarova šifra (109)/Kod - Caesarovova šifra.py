vstup = "ahojz KYč :)"
vystup_sif = "Výstup šifrování: "
vystup_desif = "Výstup dešifrování: "
posun = 3

#print(ord("a"))
#print(ord("A"))

def sifrator(input, exitus, trabea):
    for i in range(len(input)):
        ave = input[i]
        if 97<=ord(ave)<=122:
            exitus += chr((ord(ave)+ trabea - 97) %26 + 97)
        elif 65<=ord(ave)<=90:
            exitus += chr((ord(ave)+ trabea - 65) %26 + 65)
        else:
            exitus += ave
    return exitus

def desifrator(input, exitus, trabea):
    for i in range(len(input)):
        ave = input[i]
        if 97<=ord(ave)<=122:
            exitus += chr((ord(ave)- trabea - 97) %26 + 97)
        elif 65<=ord(ave)<=90:
            exitus += chr((ord(ave)- trabea - 65) %26 + 65)
        else:
            exitus += ave
    return exitus

#sifra(vstup, vystup, posun)
print(sifrator(vstup, vystup_sif, posun))
print(desifrator(vstup, vystup_desif, posun))

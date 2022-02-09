
from asyncore import read

volba_vstupu = input("Přejete si nahrát vstup jako soubor .txt? Y/N   ")
if volba_vstupu == "Y":
    with open("vstup_kod.txt", "r", encoding="utf-8") as r:
        vstup=r.read()
else:
    vstup = input("Zadejte vstupní text:")

vystup_sif = "Výstup šifrování: \n"
vystup_desif = "Výstup dešifrování: \n"
vystup_prol = ""
posun = 0

def sifrator(input, exitus, trabea):
    for i in range(len(input)):
        ave = input[i]
        if 97<=ord(ave)<=122:
            exitus += chr((ord(ave)+ trabea - 97) %26 + 97)
        elif 65<=ord(ave)<=90:
            exitus += chr((ord(ave)+ trabea - 65) %26 + 65)
        elif 48<=ord(ave)<=57:
            exitus += chr((ord(ave)+ trabea - 48) %10 + 48)
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
        elif 48<=ord(ave)<=57:
            exitus += chr((ord(ave)- trabea - 48) %10 + 48)
        else:
            exitus += ave
    return exitus

def ProlamovacKodu(input, exitus):
    trabea=0
    for trabea in range(25):
        trabea+=1
        exitus+=str(trabea)+") "
        for i in range(len(input)):
            ave = input[i]
            if 97<=ord(ave)<=122:
                exitus += chr((ord(ave)- trabea - 97) %26 + 97)
            elif 65<=ord(ave)<=90:
                exitus += chr((ord(ave)- trabea - 65) %26 + 65)
            elif 48<=ord(ave)<=57:
                exitus += chr((ord(ave)- trabea - 48) %10 + 48)
            else:
                exitus += ave
        exitus+="\n"
    return exitus

volba_procesu = input("Pokud chcete šifrovat zadejte do konzole: S \n"
"Pokud chcete dešifrovat zadejte: D \n"
"Pokud chcete dešifrovat a neznáte hodnotu posunu zadejte: P \n")
volba_vystupu = input("Přejete si vypsat výstup jako soubor .txt? Y/N   ")

if volba_procesu == "S":
    posun = int(input("Vložte hodnotu posunu: "))
    print(sifrator(vstup, vystup_sif, posun))
    if volba_vystupu == "Y":
        with open("Vystup_Sifrovani.txt", "w", encoding="utf-8") as f:
            f.write(sifrator(vstup, vystup_sif, posun))
elif volba_procesu == "D":
    posun = int(input("Vložte hodnotu posunu: "))
    print(desifrator(vstup, vystup_desif, posun))
    if volba_vystupu == "Y":
        with open("Vystup_Desifrovani.txt", "w", encoding="utf-8") as f:
            f.write(desifrator(vstup, vystup_desif, posun))
elif volba_procesu == "P":
    print(ProlamovacKodu(vstup, vystup_prol))
    if volba_vystupu == "Y":
        with open("Vystup_Prolamovace_Kodu.txt", "w", encoding="utf-8") as f:
            f.write(ProlamovacKodu(vstup, vystup_prol))
else:
    print("Zadejte pouze možnosti z nabídky výše, více toho program neumí :/")

#print(sifrator(vstup, vystup_sif, posun))
#print(desifrator(vstup, vystup_desif, posun))
#print(ProlamovacKodu(vstup, vystup_prol))


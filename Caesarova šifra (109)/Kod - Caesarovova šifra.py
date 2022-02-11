
from asyncore import read
#User choose type of input
input_choise = input("Do you want to upload the input as a file .txt? Y/N   ")
#If user choose to use .txt file as input
if input_choise == "Y":
    #Open .txt file and input it into input_data
    with open("Vstup_Kod.txt", "r", encoding="utf-8") as r:
        input_data = r.read()
else:
    input_data = input("Input text:")

output_en = "Encoding output: \n"
output_de = "Decoding output: \n"
output_br = ""
shift = 0

def encoder(input, exitus, trabea):
    #Function encrypt input text
    #Function is repeated according to the number of characters in the input
    for i in range(len(input)):
        ave = input[i]
        #Encrypt capital letter
        if 97<=ord(ave)<=122:
            exitus += chr((ord(ave)+ trabea - 97) %26 + 97)
        #Encrypt lowercase letter
        elif 65<=ord(ave)<=90:
            exitus += chr((ord(ave)+ trabea - 65) %26 + 65)
        #Encrypt numbers
        elif 48<=ord(ave)<=57:
            exitus += chr((ord(ave)+ trabea - 48) %10 + 48)
        else:
            exitus += ave
    return exitus

def decoder(input, exitus, trabea):
    #Function decrypt input text
    #Function is repeated according to the number of characters in the input
    for i in range(len(input)):
        ave = input[i]
        #Decrypt capital letter
        if 97<=ord(ave)<=122:
            exitus += chr((ord(ave)- trabea - 97) %26 + 97)
        #Decrypt lowercase letter
        elif 65<=ord(ave)<=90:
            exitus += chr((ord(ave)- trabea - 65) %26 + 65)
        #Decrypt numbers
        elif 48<=ord(ave)<=57:
            exitus += chr((ord(ave)- trabea - 48) %10 + 48)
        else:
            exitus += ave
    return exitus

def code_breaker(input, exitus):
    #Decoder using brute force method
    trabea=0
    #Try all shift options
    for trabea in range(25):
        trabea+=1
        exitus+=str(trabea)+") "
        #Function is repeated according to the number of characters in the input
        for i in range(len(input)):
            ave = input[i]
            #Decrypt capital letter
            if 97<=ord(ave)<=122:
                exitus += chr((ord(ave)- trabea - 97) %26 + 97)
            #Decrypt lowercase letter
            elif 65<=ord(ave)<=90:
                exitus += chr((ord(ave)- trabea - 65) %26 + 65)
            #Decrypt numbers
            elif 48<=ord(ave)<=57:
                exitus += chr((ord(ave)- trabea - 48) %10 + 48)
            else:
                exitus += ave
        exitus+="\n"
    return exitus

funct = input("To encrypt, type in the console: E \n"
"To decrypt, type in the console: D \n"
"To break code, type in the console: B \n")
output_file = input("Do you want to print the output as a file .txt? Y/N   ")

#If user choose to do encoding
if funct == "E":
    shift = int(input("Input shift: "))
    print(encoder(input_data, output_en, shift))
    if output_file == "Y":
        with open("Vystup_Sifrovani.txt", "w", encoding="utf-8") as f:
            f.write(encoder(input_data, output_en, shift))
#If user choose to do decoding
elif funct == "D":
    shift = int(input("Input shift: "))
    print(decoder(input_data, output_de, shift))
    if output_file == "Y":
        with open("Vystup_Desifrovani.txt", "w", encoding="utf-8") as f:
            f.write(decoder(input_data, output_de, shift))
#If user choose to do decoding by brute force method
elif funct == "B":
    print(code_breaker(input_data, output_br))
    if output_file == "Y":
        with open("Vystup_Prolamovace_Kodu.txt", "w", encoding="utf-8") as f:
            f.write(code_breaker(input_data, output_br))
else:
    print("Enter only the options from the menu above.")



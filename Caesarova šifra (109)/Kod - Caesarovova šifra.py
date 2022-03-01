
from asyncore import read
from re import A
from tkinter import N

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
A=97
a=65
Z=122
z=90
digit_zero=48
digit_nine=57

def CheckForCzech2(input):
    NonCzech = input.replace("Á",chr(ord("A")))
    print(NonCzech)
    input_data = NonCzech
    print(input_data)
    return(input_data)

def CheckForCzechs(letter):
    if ord(letter)==ord("Á"):
        letter="A"
        ave=letter
    return()
    

def encoder(input, exitus, trabea):
    #Function encrypt input text
    #Function is repeated according to the number of characters in the input
    for i in range(len(input)):
        ave = input[i]
        CheckForCzechs(ave)
        print(ave)
        #Encrypt capital letter
        if A<=ord(ave)<=Z:
            exitus += chr((ord(ave)+ trabea - A) %26 + A)
        #Encrypt lowercase letter
        elif a<=ord(ave)<=z:
            exitus += chr((ord(ave)+ trabea - a) %26 + a)
        #Encrypt numbers
        elif digit_zero<=ord(ave)<=digit_nine:
            exitus += chr((ord(ave)+ trabea - digit_zero) %10 + digit_zero)
        else:
            exitus += ave
    return exitus

def decoder(input, exitus, trabea):
    #Function decrypt input text
    #Function is repeated according to the number of characters in the input
    for i in range(len(input)):
        ave = input[i]
        #Decrypt capital letter
        if A<=ord(ave)<=Z:
            exitus += chr((ord(ave)- trabea - A) %26 + A)
        #Decrypt lowercase letter
        elif a<=ord(ave)<=z:
            exitus += chr((ord(ave)- trabea - a) %26 + a)
        #Decrypt numbers
        elif digit_zero<=ord(ave)<=digit_nine:
            exitus += chr((ord(ave)- trabea - digit_zero) %10 + digit_zero)
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
            if A<=ord(ave)<=Z:
                exitus += chr((ord(ave)- trabea - A) %26 + A)
            #Decrypt lowercase letter
            elif a<=ord(ave)<=z:
                exitus += chr((ord(ave)- trabea - a) %26 + a)
            #Decrypt numbers
            elif digit_zero<=ord(ave)<=digit_nine:
                exitus += chr((ord(ave)- trabea - digit_zero) %10 + digit_zero)
            else:
                exitus += ave
        exitus+="\n"
    return exitus

CheckForCzech2(input_data)

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



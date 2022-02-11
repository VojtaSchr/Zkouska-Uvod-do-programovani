import csv
#seznam = [4, 8, 2, 0.5, 99, -3, -1, 8]
seznam =[]

input_number=float(input("Input first number: "))
seznam = input_number
while input_number!="":
    input_number =float(input("Input one number: "))
    while input_number!="":
        seznam += input_number

print("Length of imput list is " + str(len(seznam)) + " numbers.")

def InsertSort(data):
    #Sorting funcion
    #Function is repeated according to the number of characters in the input
    for i in range(len(data)):
        a=data[i]
        o=i-1
        #When the sorted value is greater than the previous one, it moves to the left 
        while o>=0 and a<data[o]:
            data[o+1]=data[o]
            o=o-1
        data[o+1]=a  
    return()

#with open('Vstup_Sort.csv', newline='') as csvin:
#    csv.register_dialect("dialect1", delimiter=";")
#    reader = csv.reader(csvin, dialect="dialect1")
#    seznam = list(reader)
InsertSort(seznam)
print("Sorted list:", end=" ")
#Print sorted output
for i in range(len(seznam)):
    print(seznam[i], end=", ")
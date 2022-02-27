import csv
list_in = []

#User choose type of input
input_choise = input("Do you want to upload the input as a file .txt? Y/N   ")
#If user choose to use .txt file as input
if input_choise == "Y":
    #Open .txt file and input it into list_in
    try:
        with open("Vstup_Sort.txt") as txtfile:
            try:
                list_in = list(map(int, txtfile.read().split(",")))
            except ValueError:
                print("In input file is/are unsupported symbol/s. Use only numbers and split symbol.")
                quit()
    except FileNotFoundError:                           #Ošetření chyby vstupních dat
        print("File not found. Input file need to be in same folder as program. File name need to be Vstup_Sort.txt")
        quit()
    except PermissionError:                             #Ošetření chyby vstupních dat
        print("Program doesnt have permission to read input file.")
        quit()


print("Length of imput list is " + str(len(list_in)) + " numbers.")

def InsertSort(data):
    #Sorting funcion
    #Data sequence is traversed sequentially
    for i in range(len(data)):
        a=data[i]
        o=i-1
        #When the sorted value is greater than the previous one, it moves to the left 
        while o>=0 and a<data[o]:
            data[o+1]=data[o]
            o=o-1
        data[o+1]=a  
    return()

def output_in_txt(list_in):
    #Print sorted output into txt file
    with open("Vystup_Sort.txt", "w", encoding="utf-8") as f:
        for i in range(len(list_in)):
            f.write(str(list_in[i]) + ", ")
    return()

def output_in_csv(list_in):
    #Print sorted output into csv file 
    with open("Vystup_Sort.csv", "w", encoding="utf-8") as f:
        b=csv.writer(f, delimiter=";")
        b.writerow(list_in)
    return()

InsertSort(list_in)
print("Sorted list:", end=" ")
#Print sorted output
for i in range(len(list_in)):
    print(list_in[i], end=", ")

#Print sorted output into txt file
output_file_txt = input("\n Do you want to print the output as a file .txt? Y/N   ")
if output_file_txt == "Y":
    output_in_txt(list_in)


#Print sorted output into csv file            
output_file_csv = input("\n Do you want to print the output as a file .csv? Y/N   ")
if output_file_csv == "Y":
    output_in_csv(list_in)

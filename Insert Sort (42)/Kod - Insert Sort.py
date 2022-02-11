list_in = [4, 8, 2, 0.5, 99, -3, -1, 8]

print("Length of imput list is " + str(len(list_in)) + " numbers.")

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

InsertSort(list_in)
print("Sorted list:", end=" ")
#Print sorted output
for i in range(len(list_in)):
    print(list_in[i], end=", ")
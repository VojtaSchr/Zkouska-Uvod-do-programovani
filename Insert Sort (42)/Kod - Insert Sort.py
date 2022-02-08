vstup = [1, 8, 2, 99, 3]

print("Délka vstupního seznamu je " + str(len(vstup)) + " hodnot.")

def InsertSort(vstup):
    for i in range(len(vstup)):
        a=vstup[i]
        #while i>0:
        o=i-1
        while i>0 and a<vstup[o]:
            vstup[o+1]=vstup[o]
            o=o-1
        vstup[o+1]=a  
    return()

InsertSort(vstup)
print("Setřídění seznam čísel:", end=" ")
for i in range(len(vstup)):
    print(vstup[i], end=" ")
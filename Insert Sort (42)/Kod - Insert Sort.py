seznam = [4, 8, 2, 0.5, 99, -3, -1, 8]

print("Délka vstupního seznamu je " + str(len(seznam)) + " hodnot.")

def InsertSort(vstup):
    for i in range(len(vstup)):
        a=vstup[i]
        #while i>0:
        o=i-1
        while o>=0 and a<vstup[o]:
            vstup[o+1]=vstup[o]
            o=o-1
        vstup[o+1]=a  
    return()

InsertSort(seznam)
print("Setřídění seznam čísel:", end=" ")
for i in range(len(seznam)):
    print(seznam[i], end=", ")
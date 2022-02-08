vstup = [1, 8, 2, 99, 3]

print(len(vstup))

def InsertSort(vstup):
    for i in range(len(vstup)):
        a=vstup[i]
        while i>0:
            o=i-1
            while a<vstup[o]:
                vstup[o+1]=vstup[o]
                o=o-1
        i=i+1    
    return()

InsertSort(vstup)
print(len(vstup))
for i in range(len(vstup)):
    print(vstup[i])
myTable=[8, 9, 4, 6, 12, 3, 1]
print(myTable)
val1=int(input("Entrez l'indice de la première valeur à permuter.\n"))
val2=int(input("Entrez l'indice de la seconde valeur à permuter.\n"))
myTable[val1], myTable[val2]=myTable[val2], myTable[val1]
print(myTable)
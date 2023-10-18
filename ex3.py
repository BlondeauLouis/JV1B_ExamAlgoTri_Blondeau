myTable=[8, 9, 4, 6, 12, 3, 1]
print(myTable)

for j in range(len(myTable)):
    for i in range(len(myTable)-1):
        if myTable[i]>myTable[i+1]:
            myTable[i], myTable[i+1]=myTable[i+1], myTable[i]

print(myTable)
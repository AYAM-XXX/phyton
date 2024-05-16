'''subtrair vertores'''
# criar 3 vetors ABC e a sub de A - B vai ser inserido no C
# entrada: vetA[], vetB[], vetC[]
vetA = []
vetB = []
vetC = []
for x in range(20):
    vetA.append(int(input(f"digite valor vetor A[{x}]: ")))
    vetB.append(int(input(f"digite valor vetor B[{x}]:  ")))
    vetC.append(vetA[x] - vetB[x])
print("vetor A")
for x, item in enumerate(vetA):
    print(item)
print("vetor B")
for x, item in enumerate(vetB):
    print(item)
print("vetor C")
for x, item in enumerate(vetC):
    print(item)

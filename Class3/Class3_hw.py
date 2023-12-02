a = [[1, 2, 4],
     [3, 5, 7],
     [2, 4, 9]]
b = [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]
for i in b:
    print(i)
bigO = 9*9
print("O (", bigO,  ")")
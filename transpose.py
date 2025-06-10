arr = []

row=2
col=3

for i in range(row):
    a = []
    for j in range(col):
        a.append(int(input("Enter array elements:")))
    arr.append(a)

for i, row in enumerate (arr):
   for j, col in enumerate (row):
       print(arr[i][j], end=" ") 
   print()
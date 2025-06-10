n = int(input("Enter start year: "))
m = int(input("Enter end year: "))

for i in range(n, m + 1):
    if i % 4 == 0:
        print(i)

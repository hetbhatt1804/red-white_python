number = []
count = int(input("how many numbers you want in list   "))
for i in range(count):
    num = int(input("enter a number  {}: ".format(i+1)))
    number.append(num)
number.sort()
print(number)
print(number[0])
print(number[count-1])
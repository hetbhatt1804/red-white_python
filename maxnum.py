a = int(input("enter first number"))
b = int(input("enter second nmuber"))
c = int(input("enter third number"))


'''if a==b and b==c:
    print("all are same")


elif a>b:
    if a>c:
        print("a is largest number")
    else:
        print("c is greatest")
else:
    if b>c:
        print("b is greatest")
    else:
        print("c is gratest") '''

if a >= b and a>= c:
    print("The largest number is:", a)
elif b >= a and b >= c:
    print("The largest numer is:",c)
else:
    print("The largest number is:", c) 

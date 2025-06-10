num = int(input("enter a number to find cube and square"))
def outer():
    sqaure = num**2
    print(sqaure)
    def inner():
        cube = num**3
        print(cube)
    inner()   

outer()


    
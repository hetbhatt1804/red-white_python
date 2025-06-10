def outer():
    str = input("enter a string  ")
    def inner():
        print(len(str))
    inner()


outer()
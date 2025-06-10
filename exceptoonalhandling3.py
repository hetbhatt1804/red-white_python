


try:
    filename = input("enter filename")
    
    fileopen = open(filename,"r")
except:
    print("enter valid file name")
else:
    
    print(fileopen.read())       
#file = open("newfile.txt", "x")
#file.write("python is a versatile programming language")
#file = open("newfile.txt", "r")
#for i in file:
#   print(i)
    
def create_and_read_file(filename, content):
    
    file = open(filename, "x")
    file.write(content)
    file.close()


    file = open(filename, "r")
    for line in file:
        print(line)
    file.close()


create_and_read_file("newfile.txt", "python is a versatile programming language")


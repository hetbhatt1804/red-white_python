file = open("newfile.txt","r")
print(file.read())
file.close()

file = open("newfile.txt ", "a")
file.write("\n")
file.write("this is new edited line")
file = open("notes.txt", "r")


print(file.read())
file = open("notes.txt", "a")
file.write("hello")
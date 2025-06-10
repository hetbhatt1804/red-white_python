file = open("notes.txt", "r")

content = file.read()

file = open("backup.txt","x")

file=  open("backup.txt", "a")

file.write(content)
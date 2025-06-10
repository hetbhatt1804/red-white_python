file = open("notes.txt" ,"r")
content = file.read()
word = input("enter a word to search")

for i in content.split():
    if i == word:
        print(i)
    else:
        pass    
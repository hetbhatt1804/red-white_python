class Student:

#constructor
    def __init__(self):
       self.__grid = int(input("Enter GRID: "))
       self.__name = input("Enter Name: ")
       self.__age = int(input("Enter Age: "))
       self.__course = input("Enter Course: ")

# getter

    def getData(self):

       print(f"GRID: {self.__grid}, Name: {self.__name}, Age: {self.__age}, Course: {self.__course}")

s1=Student()
s2=Student()

s1.getData()
s2.getData()
class granfather():
    print("this is gradnfather class")
class father(granfather):
    print("this is father class")    
class child(father):
    print("this is child class")

class behaviour():
    super(child)
    print("this is the behaviour")    
class property():
    super(child)
    print("this is the properties")   


o1 = behaviour()
o2 = property()
class grandfather():
    print("this is grandfather")

class father(grandfather):
    print("this is father")
class child(father):
    print("this is child")    


child()
class parent():
    def Display(self):
        print("i am parent")
class child(parent):
    pass      


ob = child()
ob.Display()
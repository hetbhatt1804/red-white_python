class counter:


    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1



    def getData(self):
        print(self.count)

v = counter()
for i in range(100):
    v.getData()
    v.increment()
        


            


    
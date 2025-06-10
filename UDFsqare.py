def square(*args):
    
    squared = []
    
    for x in args:
       square = x ** 2
       squared.append(square)

    print( squared)


square(5, 3, 5, 67, 8)
  
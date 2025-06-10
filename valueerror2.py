#def event_check(a):
#    
#    if a % 2 == 0:
#        raise(ValueError)
#    else:
#        pass
#
#a = int(input("enter a number"))  
def check_event(value):
    if (value) == value:
        raise TypeError("Input must be an integer")
    if value % 2 == 0:
        raise ValueError("Input must be an odd number")
    print( "Valid odd integer")

check_event(3)
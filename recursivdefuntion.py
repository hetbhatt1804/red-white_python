def findfactorial(n):
   
    if n <= 1:
        return 1
    else:
        return n*findfactorial(n-1)
    
        

n = int(input("enter a number to find factorial                   "))
print(findfactorial(n))

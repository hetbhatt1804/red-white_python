def fibonacci(n):
    if n == 0:
      return 0
    elif n == 1:
       return 1
    elif n > 0:
       for i in range (n,0,-1):
         
          
          

         return fibonacci(i-1) + fibonacci(i-2)
    else:
       pass



    
n = int(input("enter a number  "))    
print(fibonacci(n))
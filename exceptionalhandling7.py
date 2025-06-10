try:
    num = int(input("enter a number to find its square"))
except:
    print("enter valiud number")  
else:
    print(num**2)   
finally:
    print("execution completed")      
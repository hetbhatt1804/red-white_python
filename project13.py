a = 10                  # integer
b = 10.5                # float
c = "Hello"             # string
d = True                # boolean
e = [1, 2, 3]           # list
f = (4, 5, 6)           # tuple
g = {"a": 1, "b": 2}    # dictionary

variables = [a, b, c, d, e, f, g]

for var in variables:
    print("Value:", var, "| Type:", type(var), "| Memory Address:", id(var))
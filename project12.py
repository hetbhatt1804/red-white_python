x = 200
y = 200

print("Before change:")
print("x =", x, "| id(x) =", id(x))
print("y =", y, "| id(y) =", id(y))

x = 400

print("\nAfter changing x:")
print("x =", x, "| id(x) =", id(x))
print("y =", y, "| id(y) =", id(y))
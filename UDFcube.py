def cube_numbers(numbers):
    return [n ** 3 for n in numbers]

count = int(input("How many numbers you want to cube? "))

nums = []
for i in range(count):
    num = int(input(f"Enter number {i + 1}: "))
    nums.append(num)

cubed = cube_numbers(nums)
print("Cubed values:", cubed)

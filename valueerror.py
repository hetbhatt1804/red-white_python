age = int(input("enter your age"))


if age < 18:
    raise ValueError("to vote you must be 18+ ")
else:
    print("you can vote")
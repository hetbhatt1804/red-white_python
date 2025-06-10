def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])

# Test inputs
test_strings = ["hello", "world", "recursion", "Python", ""]

for s in test_strings:
    print(f"Original: {s} -> Reversed: {reverse_string(s)}")

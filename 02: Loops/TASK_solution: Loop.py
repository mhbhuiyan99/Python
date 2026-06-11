# TASK 2A: FizzBuzz
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# More Pythonic (short-circuit)
for i in range(1, 51):
    result = ""
    if i % 3 == 0: result += "Fizz"
    if i % 5 == 0: result += "Buzz"
    print(result or i)  # If result is empty string (falsy), print i

# TASK 2B: Common elements
common = []
for x in list1:
    if x in list2 and x not in common:
        common.append(x)
print(common)

# TASK 2C: Pattern
for i in range(1, 6):
    print("*" * i)   # String multiplication!

# TASK 2D: Flatten
flat = []
for sublist in nested:
    for item in sublist:
        flat.append(item)
print(flat)

# Or using list comprehension (coming up next!)
flat = [item for sublist in nested for item in sublist]

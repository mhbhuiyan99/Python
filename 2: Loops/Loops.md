```python
# range() - generates sequence
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 2): # 2, 4, 6, 8 (start, stop, step)
    print(i)

# enumerate() - get index AND value
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# zip() - iterate multiple lists together
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Iterate dictionary
person = {"name": "Alice", "age": 25, "city": "NYC"}
for key, value in person.items():
    print(f"{key} = {value}")

# while with else (unique to Python!)
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("Loop completed normally (no break)")

# break, continue, pass
for num in range(10):
    if num == 3:
        continue      # Skip this iteration
    if num == 7:
        break         # Exit loop
    print(num)
```

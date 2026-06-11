# Basic function
def greet(name, greeting="Hello"):    # Default parameter
    return f"{greeting}, {name}!"

print(greet("Alice"))               # Hello, Alice!
print(greet("Bob", "Hi"))           # Hi, Bob!

# Multiple return values (returns tuple)
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)/len(numbers)

minimum, maximum, average = get_stats([1, 2, 3, 4, 5])

# *args - variable positional arguments
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4, 5))       # 15

# **kwargs - variable keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")

# Combining both
def flexible(*args, **kwargs):
    print(f"Positional: {args}")
    print(f"Keyword: {kwargs}")

flexible(1, 2, 3, name="Alice", age=25)

# Lambda (anonymous functions)
square = lambda x: x ** 2
print(square(5))                    # 25

# Lambda with map/filter
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))

# But comprehensions are usually preferred:
doubled = [x * 2 for x in nums]
evens = [x for x in nums if x % 2 == 0]

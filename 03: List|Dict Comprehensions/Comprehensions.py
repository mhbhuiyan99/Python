# Instead of this (C-style):
squares = []
for x in range(10):
    squares.append(x ** 2)

# Do this (Pythonic):
squares = [x ** 2 for x in range(10)]

# With condition
evens = [x for x in range(10) if x % 2 == 0]      # [0, 2, 4, 6, 8]

# Nested comprehension
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# Dict comprehension
word_lengths = {word: len(word) for word in ["apple", "banana", "cherry"]}
# {"apple": 5, "banana": 6, "cherry": 6}

# Set comprehension
unique_lengths = {len(word) for word in ["apple", "banana", "cherry", "apple"]}
# {5, 6}

# TASK 3A
squares_even = [x**2 for x in range(1, 21) if x % 2 == 0]
print(squares_even)

# TASK 3B
words = sentence.split()
word_dict = {word: len(word) for word in words}
print(word_dict)

# TASK 3C
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [x for x in range(1, 51) if is_prime(x)]
print(primes)

# TASK 3D
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)

```python
# Creating lists
nums = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]      # Python lists can hold any type

# Accessing (same as arrays, but with superpowers)
print(nums[0])        # 1
print(nums[-1])       # 5  (last element - negative indexing!)
print(nums[-2])       # 4  (second last)

# Slicing (this is huge in Python)
print(nums[1:4])      # [2, 3, 4]   (index 1 to 3)
print(nums[:3])       # [1, 2, 3]   (start to index 2)
print(nums[2:])       # [3, 4, 5]   (index 2 to end)
print(nums[::2])      # [1, 3, 5]   (every 2nd element)
print(nums[::-1])     # [5, 4, 3, 2, 1]  (REVERSED!)

# Modifying
nums.append(6)        # Add to end: [1, 2, 3, 4, 5, 6]
nums.insert(0, 0)     # Insert at index: [0, 1, 2, 3, 4, 5, 6]
nums.extend([7, 8])   # Add multiple: [0, 1, 2, 3, 4, 5, 6, 7, 8]
last = nums.pop()     # Remove & return last: last=8, nums=[...7]
first = nums.pop(0)   # Remove & return index 0: first=0
nums.remove(3)        # Remove first occurrence of value 3

# List methods
print(len(nums))      # Length
print(nums.index(5))  # Find index of value 5
print(5 in nums)      # Check existence: True/False
nums.sort()           # Sort in-place
nums.sort(reverse=True)  # Descending
sorted_nums = sorted(nums)  # Returns new sorted list (original unchanged)
```

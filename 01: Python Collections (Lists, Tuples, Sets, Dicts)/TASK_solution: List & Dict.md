```python
# TASK 1A
scores = [85, 92, 78, 65, 92, 88, 76, 92, 95, 60]

highest = max(scores)
lowest = min(scores)
average = sum(scores) / len(scores)
count_92 = scores.count(92)
high_scores = [s for s in scores if s >= 80]  # List comprehension!
scores.sort(reverse=True)

print(f"Highest: {highest}, Lowest: {lowest}")
print(f"Average: {average:.2f}")
print(f"92 appears: {count_92} times")
print(f"Scores >= 80: {high_scores}")
print(f"Sorted: {scores}")

# TASK 1B
students = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob", "age": 22, "grade": "B"},
    {"name": "Charlie", "age": 21, "grade": "A"},
    {"name": "Diana", "age": 20, "grade": "C"},
]

# 1. Grade A students
grade_a = [s["name"] for s in students if s["grade"] == "A"]
print(f"Grade A: {grade_a}")

# 2. Average age
avg_age = sum(s["age"] for s in students) / len(students)
print(f"Average age: {avg_age}")

# 3. Grade mapping
grade_map = {}
for s in students:
    grade = s["grade"]
    if grade not in grade_map:
        grade_map[grade] = []
    grade_map[grade].append(s["name"])

# Or more Pythonic with defaultdict (we'll cover later)
print(f"Grade map: {grade_map}")
```

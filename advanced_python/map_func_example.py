"""
map(function, iterable)
`function`: This is the function that you want to apply to each item of the iterable. It can be a built-in function, a lambda function, or any other callable.
`iterable`: This is the iterable that you want to process. It can be a list, a tuple, a set, a dictionary, a string, or any other iterable.
"""

# Example 01:
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9, 16, 25]

# Example 02:
words = ["hello", "world", "python"]
uppers_case = list(map(lambda s: s.upper(), words))
print(uppers_case)  # ['HELLO', 'WORLD', 'PYTHON']

# Example 03:
names = ["Alice", "Bob", "Charlie"]
length = list(map(lambda s: len(s), names))
print(length)  # [5, 3, 7]


# Example 04:
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


celsius_temps = [0, 10, 20, 30, 40]
temps = list(map(celsius_to_fahrenheit, celsius_temps))
print(temps)  # [32.0, 50.0, 68.0, 86.0, 104.0]

# Example 05:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = list(map(lambda x: x if x % 2 != 0 else None, numbers))
odd_numbers = list(filter(None, odd_numbers))  # Remove None values
print(odd_numbers)  # [1, None, 3, None, 5, None, 7, None, 9, None]

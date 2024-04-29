"""
Syntax: filter(function, iterable)
`function`: This is the function that you want to apply to each item of the iterable. It can be a built-in function, a lambda function, or any other callable.
`iterable`: This is the iterable that you want to process. It can be a list, a tuple, a set, a dictionary, a string, or any other iterable.
"""

# Example 01:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)  # [2, 4, 6, 8, 10]

# Example 02:
words = ["apple", "banana", "grape", "orange", "kiwi"]
long_words = list(filter(lambda s: len(s) > 5, words))
print(long_words)  # ['banana', 'orange']


# Example 03:
def is_positive(num):
    return num > 0


numbers = [-2, -1, 0, 1, 2, 3, 4, 5]
pos_numbers = list(filter(is_positive, numbers))
print(pos_numbers)  # [1, 2, 3, 4, 5]

# Example 04:
vowels = "aeiou"
sentence = "Hello, how are you today?"
consonants = "".join(filter(lambda char: char.lower() not in vowels, sentence))
print(consonants)  # 'Hll, hw r y tdy?'

# Example 05:
values = [10, None, 20, None, 30, 40, None]
filtered_values = list(filter(None, values))
print(filtered_values)  # Output: [10, 20, 30, 40]

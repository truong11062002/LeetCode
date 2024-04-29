"""
functools.reduce(function, iterable, initializer=None)

`function`: This is the function that you want to apply to each item of the iterable. It can be a built-in function, a lambda function, or any other callable.
`iterable`: This is the iterable that you want to process. It can be a list, a tuple, a set, a dictionary, a string, or any other iterable.
`initializer`: This is an optional argument that you can use to specify the initial value of the accumulator. If you don't provide an initializer, the first item of the iterable will be used as the initial value of the accumulator.
"""

from functools import reduce

# Example 01:
numbers = [1, 2, 3, 4, 5]

sum_result = reduce(lambda x, y: x + y, numbers)
print(sum_result)  # 1 + 2 + 3 + 4 + 5 = 15

# Example 02:
numbers = [3, 8, 1, 6, 2, 5]
max_value = reduce(lambda x, y: x if x > y else y, numbers)
print(max_value)  # 8

# Example 03:
words = ["Python", "is", "awesome"]
concat_words = reduce(lambda x, y: x + " " + y, words)
print(concat_words)  # 'Python is awesome'

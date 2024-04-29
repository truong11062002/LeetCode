"""
lambda arguments: expression
"""

square = lambda x: x**2
print(square(3))  # 3^2 = 9

add = lambda x, y: x + y
print(add(3, 4))  # 3 + 4 = 7

is_even = lambda x: x % 2 == 0
print(is_even(4))  # True

first_char = lambda s: s[0]
print(first_char("hello"))  # 'h'

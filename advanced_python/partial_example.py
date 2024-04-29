from functools import partial


# Original function
def power(base, exponent):
    return base**exponent


# Create a new function that always uses 2 as the base
square = partial(power, exponent=2)

print(square(3))  # 3^2 = 9
print(square(4))  # 4^2 = 16

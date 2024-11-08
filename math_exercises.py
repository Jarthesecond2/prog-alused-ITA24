"""Math exercises."""

import math


def sum_and_difference(num_a: int, num_b: int) -> tuple:
    """Return the sum and difference of given variables num_a and num_b."""
    # Write your code here
    sum = num_a + num_b
    difference = num_a - num_b
    return sum, difference


print(sum_and_difference(5, 2))
print(sum_and_difference(3, 3))


def float_division(num_a: int, num_b: int) -> float:
    """Divide given variables num_a and num_b and return the result."""
    division = num_a / num_b
    # Write your code here
    return division


print(float_division(8, 2))


def integer_division(num_a: int, num_b: int) -> int:
    """Divide given variables num_a and num_b and return the result rounded down."""
    # Write your code here
    division = num_a // num_b
    return division


print(integer_division(4, 2))


def powerful_operations(num_a: int, num_b: int) -> tuple:
    """Return the product of given variables, num_a to the power of num_b and the remainder of division of variables."""
    # Write your code here
    multiply_numbers = num_a * num_b
    power = num_a ** num_b
    remainder = num_a % num_b
    return multiply_numbers, power, remainder


print(powerful_operations(4, 3))


def find_average(num_a: int, num_b: int) -> float:
    """Return the average of given variables."""
    # Write your code here
    average = (num_a + num_b) / 2
    return average


print(find_average(2, 4))


def area_of_a_circle(radius: float) -> float:
    """Calculate and return the area of a circle."""
    # Write your code here
    circle_area = math.pi * radius ** 2
    return round(circle_area, 2)


print(area_of_a_circle(2))


def area_of_an_equilateral_triangle(side_length: float) -> float:
    """Calculate and return the area of an equilateral triangle, rounded to the nearest whole number."""
    triangle_area = (math.sqrt(3) / 4) * side_length ** 2
    return round(triangle_area)


print(area_of_an_equilateral_triangle(4))


def calculate_discriminant(a: int, b: int, c: int) -> int:
    """Calculate discriminant with given variables and return the result."""
    # Write your code here
    discriminant = b ** 2 - 4 * a * c
    return discriminant


print(calculate_discriminant(9, 10, 1))


def calculate_hypotenuse_length(a: int, b: int) -> float:
    """Return the length of hypotenuse when the lengths of the catheti are given."""
    # Write your code here
    c = math.sqrt(a ** 2 + b ** 2)
    return c


print(calculate_hypotenuse_length(3, 4))


def calculate_cathetus_length(a: int, c: int) -> float:
    """Return the length of cathetus when the lengths of the second cathetus and hypotenuse are given."""
    # Write your code here
    b = math.sqrt(c ** 2 - a ** 2)
    return b


print(calculate_cathetus_length(3, 5))
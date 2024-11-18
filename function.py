"""Function examples."""


# func()


def func():
    """Print a message indicating that the function is running."""
    print("I´m inside the function")


# my_name_is(name)


def my_name_is(name):
    """Print the provided name with a greeting."""
    print("My name is " + name)


my_name_is("Mari")


# sum_six(num)


def sum_six(num):
    """Add six to the provided number."""
    return num + 6


print(sum_six(2))


# sum_numbers()


def sum_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b


c = sum_numbers(2, 4)
print(c)


# usd_to_eur()


def usd_to_eur(amount):
    """Convert USD to EUR at an 0.8 conversion rate."""
    return amount * 0.8


print(usd_to_eur(3))
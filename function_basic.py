"""Basic function exercises."""
import math


def print_hello():
    """Print "hello"."""
    # code here
    print("Hello")


print_hello()


def get_hello() -> str:
    """Return "hello"."""
    # code here
    return "Hello"


get_hello()


def ask_name_and_greet_user():
    """
    Ask name and greet user.

    The user has to enter his/her name. The function prints the greeting.

    Regular greeting: Hi, [name]. Would you like to have a Hamburger?
    [name] is capitalized, meaning first letter is capital, the rest is lower.

    If the name is Thanos (case insensitive, so thanos and THANOS also count):
    Get out of here, Thanos! Nobody wants to play with you!
    """
    # code here
    name = input("Please enter your name: ")
    capitalized_name = name.capitalize()

    if capitalized_name.lower() == "thanos":
        print("Get out of here, Thanos! Nobody wants to play with you!")
    else:
        print(f"Hi, {capitalized_name}. Would you like to have a Hamburger?")


def calculate_hypotenuse_length(a: float, b: float) -> float:
    """Return hypotenuse value."""
    # code here
    return math.sqrt(a ** 2 + b ** 2)


c = calculate_hypotenuse_length(10, 10)
print(c)


def calculate_cathetus_length(a: float, c: float) -> float:
    """Return cathetus value."""
    # code here
    return math.sqrt(c ** 2 - a ** 2)


b = calculate_cathetus_length(5, 7)
print(b)


if __name__ == '__main__':
    print_hello()  # should print "Hello"
    hello = get_hello()  # should return "Hello"
    print(hello)  # let's check the value of hello variable
    ask_name_and_greet_user()  # should ask name and greet
    print(calculate_hypotenuse_length(3, 4))  # should print 5.0
    print(calculate_cathetus_length(3, 5))  # should print 4.0
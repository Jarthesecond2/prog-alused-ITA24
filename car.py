"""Car operations."""
current_year = 2025


class Car:
    """Car object."""

    def __init__(self, model, year, price):
        """Car constructor."""
        self.year = year
        self.model = model
        self.price = price


def create_car(model: str, price: int) -> 'Car':
    """Create a new car object with the current year if price is above 0."""
    if price > 0:
        return Car(model, current_year, price)
    return None


def get_most_expensive_car_below_price(cars: list, max_price: int) -> 'Car':
    """
    Return the most expensive car with the price lower than max_price.

    If several cars have the same price, return the first.
    If there are no cars with which have the price lower than max_price, return None.
    """
    eligible_cars = [car for car in cars if car.price < max_price]
    return max(eligible_cars, key=lambda car: car.price, default=None)


def update_prices(cars: list, discount_per_year: int) -> None:
    """
    Update each car price so that for every year of their age they get discount_per_year lower price.

    If the car year is 2018 and currently it's 2020, then the discount is applied twice.
    The car price can never go below 0.

    Example:
        Currently it's 2020

        Car year is 2015
        Car price is 100
        discount_per_year = 5
        The new price for the car is 75

        Car year is 2000, price is 100, discount_per_year = 7
        The new price for the car is 0.
    """
    for car in cars:
        years_old = current_year - car.year
        new_price = max(0, car.price - years_old * discount_per_year)
        car.price = new_price


def get_cars_with_model(cars: list, model: str) -> list:
    """Return list of cars with the given model."""
    return [car for car in cars if car.model == model]


def get_ordered_cars(cars: list) -> list:
    """Return a new sorted list of cars by: year (newer first), price (cheaper first), model (from a to z)."""
    return sorted(cars, key=lambda car: (-car.year, car.price, car.model))
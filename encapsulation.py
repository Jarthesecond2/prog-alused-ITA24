"""Encapsulation exercise."""


class Student:
    """Represent student with name, id and status."""

    def __init__(self, name, student_id):
        """Algatab tudengi objekti."""
        self.__name = name
        self.__student_id = student_id
        self.__status = "Active"

    def get_id(self):
        """Tagastab tudengi ID."""
        return self.__student_id

    def set_name(self, name):
        """Määrab tudengile uue nime."""
        self.__name = name

    def get_name(self):
        """Tagastab tudengi nime."""
        return self.__name

    def set_status(self, status):
        """
        Määrab tudengile uue staatuse.

        Staatust muudetakse vaid siis, kui see on kehtiv.
        """
        valid_statuses = ["Active", "Expelled", "Finished", "Inactive"]
        if status in valid_statuses:
            self.__status = status

    def get_status(self):
        """Tagastab tudengi staatuse."""
        return self.__status

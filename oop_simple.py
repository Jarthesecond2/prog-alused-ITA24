"""Simple class."""


class Student:
    """Klass Student, mis sisaldab üliõpilase nime ja lõpetamise olekut."""

    def __init__(self, name):
        """
        Konstruktor, mis määrab üliõpilase nime ja lõpetamise oleku.

        :param name: Üliõpilase nimi.
        """
        self.name = name
        self.finished = False


student = Student("John")
print(student.name)
print(student.finished)
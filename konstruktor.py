"""Constructor exercise."""


class Empty:
    """Klass Empty ei oma konstruktorit. Kasutatakse vaikimisi konstruktorit."""

    pass


class Person:
    """
    Klass Person, millel on konstruktor, mis määrab eesnime, perenime ja vanuse.

    Konstruktor määrab vaikeväärtused: "", "", 0.
    """

    def __init__(self):
        """
        Konstruktor, mis määrab Person objekti väljad: firstname, lastname ja age.

        Vaikeväärtused on "", "", 0.
        """
        self.firstname = ""
        self.lastname = ""
        self.age = 0


class Student:
    """
    Klass Student, millel on konstruktor, mis võtab vastu eesnime, perenime ja vanuse.

    Need väärtused salvestatakse objekti juurde.
    """

    def __init__(self, firstname: str, lastname: str, age: int):
        """
        Konstruktor, mis määrab Student objekti väljad: firstname, lastname ja age.

        :param firstname: Üliõpilase eesnimi
        :param lastname: Üliõpilase perenimi
        :param age: Üliõpilase vanus
        """
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


if __name__ == '__main__':
    empty_object = Empty()

    person1 = Person()
    person1.firstname = "Mati"
    person1.lastname = "Kaal"
    person1.age = 30

    person2 = Person()
    person2.firstname = "Kati"
    person2.lastname = "Maal"
    person2.age = 25

    person3 = Person()
    person3.firstname = "Jaan"
    person3.lastname = "Tamm"
    person3.age = 28

    student1 = Student("Mati", "Kaal", 20)
    student2 = Student("Kati", "Maal", 22)
    student3 = Student("Jaan", "Tamm", 23)

    print(f"Person 1: {person1.firstname} {person1.lastname}, Age: {person1.age}")
    print(f"Person 2: {person2.firstname} {person2.lastname}, Age: {person2.age}")
    print(f"Person 3: {person3.firstname} {person3.lastname}, Age: {person3.age}")
    print(f"Student 1: {student1.firstname} {student1.lastname}, Age: {student1.age}")
    print(f"Student 2: {student2.firstname} {student2.lastname}, Age: {student2.age}")
    print(f"Student 3: {student3.firstname} {student3.lastname}, Age: {student3.age}")
"""Student class with student name and grades."""


class Student:
    """
    Esindab kooli õpilast.

    Omadused:
        name (str): Õpilase nimi.
        id (int): Õpilase unikaalne ID.
        grades (list[tuple]): Järjend, mis sisaldab kursusi ja hindeid.
    """

    def __init__(self, name: str):
        """
        Loob uue õpilase.

        Argumendid:
            name (str): Õpilase nimi.
        """
        self.name = name
        self.id = None
        self.grades = []

    def set_id(self, id: int):
        """
        Määrab õpilasele unikaalse ID. Kui ID on juba määratud, siis seda ei muudeta.

        Argumendid:
            id (int): Õpilase unikaalne ID.
        """
        if self.id is None:
            self.id = id

    def get_id(self) -> int:
        """
        Tagastab õpilase ID.

        Tagastab:
            int: Õpilase unikaalne ID.
        """
        return self.id

    def add_grade(self, course, grade: int):
        """
        Lisab õpilasele hinde konkreetse kursuse eest.

        Argumendid:
            course (Course): Kursuse objekt.
            grade (int): Õpilase hinne kursusel.
        """
        self.grades.append((course, grade))

    def get_grades(self) -> list[tuple]:
        """
        Tagastab õpilase hinded ja kursused.

        Tagastab:
            list[tuple]: Järjend, kus iga element on ennik (kursus, hinne).
        """
        return self.grades

    def get_average_grade(self) -> float:
        """
        Arvutab õpilase keskmise hinde.

        Tagastab:
            float: Õpilase keskmine hinne. Kui hindeid pole, tagastatakse -1.
        """
        if not self.grades:
            return -1
        return sum(grade for _, grade in self.grades) / len(self.grades)

    def __repr__(self):
        """
        Tagastab õpilase esindusliku tekstilise kujutise.

        Tagastab:
            str: Õpilase nimi.
        """
        return self.name

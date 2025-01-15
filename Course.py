"""Course class with name and grades."""


class Course:
    """
    Esindab kooli kursust.

    Omadused:
        name (str): Kursuse nimi.
        grades (list[tuple]): Järjend, mis sisaldab õpilasi ja nende hindeid.
    """

    def __init__(self, name: str):
        """
        Loob uue kursuse.

        Argumendid:
            name (str): Kursuse nimi.
        """
        self.name = name
        self.grades = []

    def add_grade(self, student, grade: int):
        """
        Lisab kursusele õpilase hinde.

        Argumendid:
            student (Student): Õpilase objekt.
            grade (int): Õpilase hinne kursusel.
        """
        self.grades.append((student, grade))

    def get_grades(self) -> list[tuple]:
        """
        Tagastab kursuse hinded.

        Tagastab:
            list[tuple]: Järjend, kus iga element on ennik (õpilane, hinne).
        """
        return self.grades

    def get_average_grade(self) -> float:
        """
        Arvutab kursuse keskmise hinde.

        Tagastab:
            float: Kursuse keskmine hinne. Kui hindeid pole, tagastatakse -1.
        """
        if not self.grades:
            return -1
        return sum(grade for _, grade in self.grades) / len(self.grades)

    def __repr__(self):
        """
        Tagastab kursuse esindusliku tekstilise kujutise.

        Tagastab:
            str: Kursuse nimi.
        """
        return self.name

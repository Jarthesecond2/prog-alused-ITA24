"""School class which stores information about courses and students."""


class School:
    """
    Esindab kooli, kus on õpilased ja kursused.

    Omadused:
        name (str): Kooli nimi.
        students (list[Student]): Järjend õpilastest koolis.
        courses (list[Course]): Järjend kursustest koolis.
        next_student_id (int): Järgmine vaba unikaalne ID, mida õpilasele määrata.
    """

    def __init__(self, name: str):
        """
        Loob uue kooli.

        Argumendid:
            name (str): Kooli nimi.
        """
        self.name = name
        self.students = []
        self.courses = []
        self.next_student_id = 1

    def add_course(self, course):
        """
        Lisab kooli uue kursuse. Juba olemasolevaid kursuseid ei lisata uuesti.

        Argumendid:
            course (Course): Kursuse objekt.
        """
        if course not in self.courses:
            self.courses.append(course)

    def add_student(self, student):
        """
        Lisab kooli uue õpilase.Juba olemasolevaid õpilasi ei lisata uuesti.

        Määrab õpilasele unikaalse ID.

        Argumendid:
            student (Student): Õpilase objekt.
        """
        if student not in self.students:
            student.set_id(self.next_student_id)
            self.students.append(student)
            self.next_student_id += 1

    def add_student_grade(self, student, course, grade: int):
        """
        Lisab õpilasele hinde kindla kursuse eest.

        Argumendid:
            student (Student): Õpilase objekt.
            course (Course): Kursuse objekt.
            grade (int): Hinne.
        """
        if student in self.students and course in self.courses:
            student.add_grade(course, grade)
            course.add_grade(student, grade)

    def get_students(self) -> list:
        """
        Tagastab kooli õpilaste järjendi.

        Tagastab:
            list[Student]: Järjend õpilaste objektidest.
        """
        return self.students

    def get_courses(self) -> list:
        """
        Tagastab kooli kursuste järjendi.

        Tagastab:
            list[Course]: Järjend kursuste objektidest.
        """
        return self.courses

    def get_students_ordered_by_average_grade(self) -> list:
        """
        Tagastab õpilased, järjestatuna keskmise hinde järgi kahanevalt.

        Tagastab:
            list[Student]: Järjend õpilaste objektidest, järjestatuna keskmise hinde järgi.
        """
        return sorted(self.students, key=lambda s: s.get_average_grade(), reverse=True)

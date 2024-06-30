from people import *


class Class:
    def __init__(self, grade: int, letter: str, homeroom_teacher: Teacher, students=None):
        self._grade = grade
        self._letter = letter
        self._homeroom_teacher = homeroom_teacher
        self._students = []

    def add_student(self, student):
        self._students.append(student)

    def __getitem__(self, name: str) -> List[Student]:
        return [student for student in self._students
                if student.name.startswith(name) or student.last_name.startswith(name)]

    def __iter__(self):
        return iter(sorted(self._students, key=lambda student: (student.last_name, student.name)))

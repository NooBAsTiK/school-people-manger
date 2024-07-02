import csv
from human import *


class Class:
    def __init__(self, grade: int, letter: str, homeroom_teacher: Teacher = None, students=None):
        if students is None:
            students = []
        self._grade = grade
        self._letter = letter
        self.homeroom_teacher = homeroom_teacher
        self.students = sorted(list(students), key=lambda student: (student.last_name, student.name))

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if not 1 <= value <= 11:
            raise ValueError("Класс должен быть от 1 до 11")
        self._grade = value

    @property
    def letter(self):
        return self._letter

    @letter.setter
    def letter(self, value):
        if not (len(value) == 1 and value.isupper() and 'А' <= value <= 'Я'):
            raise ValueError("Буква класса должна быть одной заглавной русской буквой")
        self._letter = value

    def add_student(self, student: Student):
        self.students.append(student)
        student.set_class(self)
        self.students = sorted(self.students, key=lambda student_new: (student_new.last_name, student_new.name))

    def find_student_by_substring(self, substring):
        found_students = [student for student in self.students if substring.lower() in student.name.lower() or substring.lower() in student.last_name.lower()]
        return found_students

    def get_students_sorted_by_last_name(self):
        return sorted(self.students, key=lambda student: student.last_name)

    def __getitem__(self, name: str):
        return [student for student in self.students if
                student.name.startswith(name) or student.last_name.startswith(name)]

    def __iter__(self):
        return iter(self.students)

    def __repr__(self):
        students_repr = ', '.join(repr(student) for student in self.students)
        return f"Класс (Номер класса = '{self.grade}', Буква класса = '{self.letter}', Учитель класса = '{self.homeroom_teacher}', Обучаемые = [{students_repr}])"

    @staticmethod
    def write_csv(filename, class_instance):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Имя', 'Фамилия', 'Класс', 'Учитель класса'])
            teacher_info = f"{class_instance.homeroom_teacher.name} {class_instance.homeroom_teacher.last_name}"
            for student in class_instance.students:
                class_info = f"{class_instance.grade}{class_instance.letter}"
                writer.writerow([student.name, student.last_name, class_info, teacher_info])

    def read_csv(filename):
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Пропускаем заголовок
            students = []
            grade, letter, homeroom_teacher = None, None, None
            for name, last_name, class_info, teacher_info in reader:
                if class_info:
                    grade, letter = int(class_info[:-1]), class_info[-1]
                if teacher_info and not homeroom_teacher:
                    teacher_info_parts = teacher_info.split(' ')
                    teacher_name = teacher_info_parts[0]
                    teacher_last_name = teacher_info_parts[1]
                    teacher_subjects = teacher_info_parts[2:]
                    homeroom_teacher = Teacher(teacher_name, teacher_last_name, teacher_subjects)
                student = Student(name, last_name)
                students.append(student)
            return Class(grade=grade, letter=letter, students=students, homeroom_teacher=homeroom_teacher)

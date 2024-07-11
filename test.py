import unittest
from my_class import *
from const import *
class TestSchoolClasses(unittest.TestCase):

    def setUp(self):
        # Создание учителя
        self.teacher = Teacher('Иван', 'Иванов', [Subject.MATH, Subject.PHYSICS])
        # Создание класса
        self.class_instance = Class(grade=5, letter='А', homeroom_teacher=self.teacher)

    def test_add_student(self):
        # Добавление учеников
        student1 = Student('Алексей', 'Смирнов')
        student2 = Student('Борис', 'Иванов')
        self.class_instance.add_student(student1)
        self.class_instance.add_student(student2)

        # Проверка, что ученики добавлены
        self.assertIn(student1, self.class_instance.students)
        self.assertIn(student2, self.class_instance.students)

    def test_lastname_sort(self):
        # Добавление учеников в произвольном порядке
        student1 = Student('Алексей', 'Смирнов')
        student2 = Student('Борис', 'Иванов')
        student3 = Student('Виктор', 'Петров')
        self.class_instance.add_student(student2)
        self.class_instance.add_student(student3)
        self.class_instance.add_student(student1)
        sorted_students = self.class_instance.get_students_sorted_by_last_name()
        expected_sorted_students = sorted(self.class_instance.students, key=lambda student: student.last_name)
        self.assertEqual(sorted_students, expected_sorted_students)

    def test_find_student_by_substring(self):
        # Добавление учеников
        student1 = Student('Алексей', 'Смирнов')
        student2 = Student('Борис', 'Иванов')
        student3 = Student('Виктор', 'Петров')
        self.class_instance.add_student(student1)
        self.class_instance.add_student(student2)
        self.class_instance.add_student(student3)

        # Поиск ученика по подстроке
        found_students = self.class_instance.find_student_by_substring('икт')
        self.assertIn(student3, found_students)
        self.assertNotIn(student1, found_students)
        self.assertNotIn(student2, found_students)

    def test_grade_setter(self):
        # Проверка установки корректного значения класса
        self.class_instance.grade = 6
        self.assertEqual(self.class_instance.grade, 6)

        # Проверка вызова исключения при некорректном значении
        with self.assertRaises(ValueError):
            self.class_instance.grade = 12

    def test_letter_setter(self):
        # Проверка установки корректного значения буквы класса
        self.class_instance.letter = 'Б'
        self.assertEqual(self.class_instance.letter, 'Б')

        # Проверка вызова исключения при некорректном значении
        with self.assertRaises(ValueError):
            self.class_instance.letter = '1'

    def test_repr_method(self):
        # Проверка работы метода __repr__
        student = Student('Алексей', 'Смирнов')
        self.class_instance.add_student(student)
        class_repr = repr(self.class_instance)
        self.assertIn("Ученик (Имя = 'Алексей', Фамилия = 'Смирнов')", class_repr)


if __name__ == '__main__':
    unittest.main()
from my_class import *
from const import *


# Создание объектов учителей
teacher_1 = Teacher(name='Иван', last_name='Петров', subjects=[Subject.MATH, Subject.PHYSICS])
teacher_2 = Teacher(name='Мария', last_name='Иванова', subjects=[Subject.RUS_LANG, Subject.HISTORY])

# Создание объектов учеников
student_1 = Student(name='Иван', last_name='Иванов')
student_2 = Student(name='Светлана', last_name='Кузнецова')
student_3 = Student(name='Дмитрий', last_name='Попов')

# Создание объекта класса
class_1A = Class(grade=1, letter='А', homeroom_teacher=teacher_1)

# Добавление учеников в класс
class_1A.add_student(student_1)
class_1A.add_student(student_2)
class_1A.add_student(student_3)

# Вывод информации о классе
print(class_1A)

# Ищем учеников, чьи имена или фамилии содержат подстроку 'ива'
found_students = class_1A.find_student_by_substring('Св')

# Выводим информацию о найденных учениках
for student in found_students:
    print(student)

sorted_students = class_1A.get_students_sorted_by_last_name()

# Выводим отсортированный список
for student in sorted_students:
    print(student)

# Запись данных в файл
class_1A = Class.write_csv('class_1A.csv', class_1A)

# Чтение данных из файла
class_1A = Class.read_csv('class_1A.csv')
# Выводим информацию о классе
print(class_1A)

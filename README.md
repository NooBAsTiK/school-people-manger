# school-people-manger
Менеджер школьных классов

## ЗАДАНИЕ

Подготовьте эти классы к дальнейшей работе:

1.  Добавьте предметов в класс предметов
2.  Человек должен инициализироваться именем и фамилией
3.  Школьники в инициализацию могут принимать ещё и класс (не обязательно)
4.  Школьникам можно менять класс через set_class и читать их класс через get_class
5.  Преподаватель в инициализацию принимает контейнер предметов, которые ведёт
6.  Преподавателям можно менять класс через set_class и читать их класс через get_class
7.  Класс инициализируется с передачей классного руководителя и итерируемый объект, содержащий детей (возможно пустого).
    При вызове методов "листа" - работает с набором школьников
9.  Класс при обращении по [ ] - ищет среди детей подходящих. Внутрь [ ] передаётся строка, возвращаются все дети,
    у которых имя или фамилия начинается с переданной строки
10. При итерации по классу - проходим по школьникам в алфавитном порядке
11. Если ещё не сделали, будет так же полезно уметь сортировать людей! Реализуйте метод __lt__, определяющий поведение
    оператора < (а так же через него оприделяются и <, <=, >= и т.д.). Будем считать что один человек меньше другого
    если у него ФИО идёт в другом порядке.
12. В человека нужно добавить поле __id. Это поле будет итендификатором, который будет отличать двух людей, даже если их
    ФИО будет совпадать (не забывайте что есть тёски!). Попытайтесь хранить внутри класса Human все уже существующие id
    в сессии интерпритатора, в конструктор человека добавьте ключевое поле id=None. Если id не передаётся - возьмите
    любое id еще не занятое (проверить это можно обратившись к информации в классе, которую вы сохраните), и выдайте
    новому объекту уникальный __id. Если поле __id уже передано, то если такого id ещё не было у человека - создайте
    с переданным id, иначе - бросьте ошибку raise Exceprion("Переданный id уже существует!")
13. В человека нужно добавить функционал хеширования __hash__(будет полезно если мы хотим сделать человека ключем
    в словаре или положить его в множество), его можно генерировать или из __id, или просто из ФИО
14. На основе этого создайте запись и чтения и записи объекта типа Сlass на диск. Предлагаемый путь - сделать два
    статических метода класса - Class.read_csv(filename) и Class.write_csv(filename). Ваша задача - попробовать уместить
    информацию о группе детей и преподавателе внутри файла, чтобы можно было завершить сессию, начать её заного, и из
    файла восстановить класс! Изначально рекомендую вам попробовать записать только информацию о наборе школьников, без
    преподавателя, номера и буквы класса. Далее можете попробовать добавить функционал с информацией о преподавателе.
15. Добавить __repr__ и __str__ всем классам доступным извне
16. Заменить букву и цифру группы с переменных на property, и проверять что буква - это одна заглавная русская буква,
    а цифра - от 1 до 11

* Для хранения будем использовать CSV файлы (текстовые файлы со структурой, которая удобно интерпритируется в таблицу).

Добавлен файл test.py для тестирования кода:
- Тест на добавление учеников 
- Тест на проверку сортировки по фамилии 
- Тест на поиск учеников по буквам 
- Тест на проверку указания правильного числа для класса (от 1 до 11)
- Тест на проверку корректности буквы класса 
- Тест на корректность вывода Имени и Фамилии ученика

Примеры использования кода с подстановкой в main.py:

```pycon
# Создание учителей с привязкой предметов
teacher_1 = Teacher(name='Юрий', last_name='Кузнецов', subjects=[Subject.MATH, Subject.PHYSICS])
teacher_2 = Teacher(name='Юлия', last_name='Амерханова', subjects=[Subject.RUS_LANG, Subject.HISTORY])
```
```pycon
# Создание класса с привязкой к учителю
class_1A = Class(grade=1, letter='А', homeroom_teacher=teacher_1)
```
```pycon
# Создание учеников
student_1 = Student(name='Иван', last_name='Петров')
student_2 = Student(name='Светлана', last_name='Иванова')
student_3 = Student(name='Дмитрий', last_name='Фуфаев')
```
```pycon
# Добавление учеников в класс
class_1A.add_student(student_1)
class_1A.add_student(student_2)
class_1A.add_student(student_3)
```
```pycon
# Вывод информации о классе
print(class_1A)

# Пример вывода в консоль
Класс (Номер класса = '1', Буква класса = 'А', Учитель класса = 'Иван Петров', Обучаемые = 
[Ученик (Имя = 'Иван', Фамилия = 'Иванов'), Ученик (Имя = 'Светлана', Фамилия = 'Кузнецова'),
Ученик (Имя = 'Дмитрий', Фамилия = 'Попов')])
```
```pycon
# Ищем учеников, чьи имена или фамилии содержат подстроку
found_students = class_1A.find_student_by_substring('Св')

# Выводим информацию о найденных учениках
for student in found_students:
    print(student)
    
# Пример вывода в консоль   
"""
Светлана Кузнецова
"""
```

```pycon
# Сортировка по фамилии с выводом списка в консоль
sorted_students = class_1A.get_students_sorted_by_last_name()

# Выводим отсортированный список
for student in sorted_students:
    print(student)
    
"""
Иван Иванов
Светлана Кузнецова
Дмитрий Попов
"""

```
```pycon
# Запись данных в файл
class_1A = Class.write_csv('class_1A.csv', class_1A)

# Чтение данных из файла
class_1A = Class.read_csv('class_1A.csv')

# Выводим информацию о классе
print(class_1A)

"""
# Пример вывода в консоль
Класс (Номер класса = '1', Буква класса = 'А', Учитель класса = 'Иван Петров', Обучаемые =
[Ученик (Имя = 'Иван', Фамилия = 'Иванов'), Ученик (Имя = 'Светлана', Фамилия = 'Кузнецова'),
Ученик (Имя = 'Дмитрий', Фамилия = 'Попов')])
"""
```
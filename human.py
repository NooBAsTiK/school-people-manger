from typing import Iterable
from const import Subject


class Human:
    _ids = set()

    def __init__(self, name: str, last_name: str, my_id=None):
        self.name = name
        self.last_name = last_name
        self.__id = my_id or self._generate_id()

    @classmethod
    def _generate_id(cls):
        new_id = 1
        while new_id in cls._ids:
            new_id += 1
        cls._ids.add(new_id)
        return new_id

    def __lt__(self, other):
        return (self.last_name, self.name) < (other.last_name, other.name)

    def __hash__(self):
        return hash((self.name, self.last_name, self.__id))

    def __repr__(self):
        return f"Человек (Имя = '{self.name}', Фамилия = '{self.last_name}', id={self.__id})"

    def __str__(self):
        return f"{self.name} {self.last_name}"


# Класс для ученика
class Student(Human):
    def __init__(self, name: str, last_name: str, class_=None):
        super().__init__(name, last_name)
        self.class_ = class_

    def set_class(self, class_):
        self.class_ = class_

    def get_class(self):
        return self.class_

    def __repr__(self):
        return f"Ученик (Имя = '{self.name}', Фамилия = '{self.last_name}')"


# Класс для учителя
class Teacher(Human):
    def __init__(self, name: str, last_name: str, subjects: Iterable[Subject]):
        super().__init__(name, last_name)
        self.subjects = list(subjects)
        self.class_ = None

    def set_class(self, class_):
        self.class_ = class_

    def get_class(self):
        return self.class_

    def __repr__(self):
        return f"Учитель(Имя = '{self.name}', Фамилия = '{self.last_name}', Предмет(ы) = {self.subjects})"

from typing import List
from subjects import *


class Human:
    def __init__(self, name: str, last_name: str):
        self.name = name
        self.last_name = last_name


class Student(Human):
    def __init__(self, name: str, last_name: str, class_: 'Class' = None):
        super().__init__(name, last_name)
        self._class = class_

    def set_class(self, class_: 'Class'):
        self._class = class_

    def get_class(self) -> 'Class':
        return self._class


class Teacher(Human):
    def __init__(self, name: str, last_name: str, subjects: List[Subject], homeroom_class: 'Class' = None):
        super().__init__(name, last_name)
        self._subjects = subjects
        self._homeroom_class = homeroom_class

    def set_class(self, class_: 'Class'):
        self._homeroom_class = class_

    def get_class(self) -> 'Class':
        return self._homeroom_class

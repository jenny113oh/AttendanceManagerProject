from abc import ABC, abstractmethod


class Grade(ABC):
    def __init__(self):
        self.grade = ''

    @abstractmethod
    def get_grade(self):
        pass

class GoldGrade(Grade):
    def __init__(self):
        super().__init__()
        self.grade = 'GOLD'

    def get_grade(self):
        return self.grade


class SilverGrade(Grade):
    def __init__(self):
        super().__init__()
        self.grade = 'SILVER'

    def get_grade(self):
        return self.grade

class NormalGrade(Grade):
    def __init__(self):
        super().__init__()
        self.grade = 'NORMAL'

    def get_grade(self):
        return self.grade

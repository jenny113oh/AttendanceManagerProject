from member_grade import NormalGrade,SilverGrade,GoldGrade

class Member:
    def __init__(self, name: str, mem_id: int):
        self._name = name
        self._id = mem_id
        self._point = 0
        self._grade = NormalGrade()
        self._cnt_wed = 0
        self._cnt_weekend = 0

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def point(self):
        return self._point

    def add_point(self, point):
        self._point += point

    @property
    def grade(self):
        return self._grade
    @grade.setter
    def grade(self, grade):
        self._grade = grade

    @property
    def cnt_wed(self):
        return self._cnt_wed

    def add_cnt_wed(self):
        self._cnt_wed += 1

    @property
    def cnt_weekend(self):
        return self._cnt_weekend

    def add_cnt_weekend(self):
        self._cnt_weekend += 1
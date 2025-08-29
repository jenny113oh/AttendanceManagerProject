from member_grade import GoldGrade, SilverGrade, NormalGrade
from member import Member

class AttendanceManager:
    def __init__(self):
        self.member_map = {}
        self.member_name_list = []
        self._member_cnt = 0

    def member_cnt(self):
        return self._member_cnt

    def member_name(self,id: int):
        return self.member_name_list[id]

    def add_member(self, name: str):
        if name in self.member_map:
            return

        self._member_cnt += 1
        self.member_name_list.insert(self._member_cnt, name)
        self.member_map[name] = Member(name, self._member_cnt)
        return

    def add_point(self, name: str, attend_day:str):
        member = self.member_map.get(name)
        if member is None:
            return

        if attend_day == 'wednesday':
            member.add_point(3)
            member.add_cnt_wed()
        elif attend_day == 'saturday' or attend_day == 'sunday':
            member.add_point(2)
            member.add_cnt_weekend()
        else :
            member.add_point(1)
        return

    def add_bonus_point(self):
        for i in range(self._member_cnt):
            member_name = self.member_name_list[i]
            member = self.member_map.get(member_name)
            if member is None:
                return
            if member.cnt_wed > 9:
                member.add_point(10)
            if member.cnt_weekend > 9:
                member.add_point(10)
        return


    def upgrade_member_grades(self):
        for i in range(self._member_cnt):
            member_name = self.member_name_list[i]
            member = self.member_map.get(member_name)

            if member.point >= 50:
                member.grade = GoldGrade()
            elif member.point >= 30:
                member.grade = SilverGrade()
            else :
                member.grade = NormalGrade()
        return

    def string_member_info(self, id: int):
        member = self.member_map.get(self.member_name_list[id])
        return f"NAME : {member.name}, POINT : {member.point}, GRADE : {member.grade.get_grade()}"

    def is_valid_member(self, id: int):
        member = self.member_map.get(self.member_name_list[id])
        if isinstance(member.grade, NormalGrade) and member.cnt_wed == 0  and member.cnt_weekend == 0 :
            return False
        return True
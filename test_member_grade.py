from member_grade import GoldGrade, SilverGrade, NormalGrade, Grade


def test_gold_grade():
    grade = GoldGrade()
    assert grade.get_grade() == 'GOLD'

def test_silver_grade():
    grade = SilverGrade()
    assert grade.get_grade() == 'SILVER'

def test_normal_grade():
    grade = NormalGrade()
    assert grade.get_grade() == 'NORMAL'


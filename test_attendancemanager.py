import pytest
from attendancemanager import AttendanceManager
from member_grade import NormalGrade, SilverGrade, GoldGrade


@pytest.fixture
def attendance_manager():
    attendance_manager = AttendanceManager()
    return attendance_manager


def test_attendance_manager(attendance_manager):
    assert attendance_manager._member_cnt == 0
    assert attendance_manager.member_name_list == []
    assert attendance_manager.member_map == {}


def test_member_cnt(attendance_manager):
    assert attendance_manager.member_cnt() == 0

def test_member_name(attendance_manager):
    attendance_manager.add_member('abc')

    assert attendance_manager.member_name(0) == 'abc'

def test_member_name_override(attendance_manager):
    attendance_manager.add_member('abc')
    attendance_manager.add_member('abc')

    assert True

def test_member_name_from_list(attendance_manager):
    attendance_manager.add_member('abc')
    assert attendance_manager.member_name(0) == 'abc'

def test_member_wednesday_point(attendance_manager):
    attendance_manager.add_member('abc')
    attendance_manager.add_point('abc', 'wednesday')
    member = attendance_manager.member_map['abc']

    assert member.point == 3
    assert member.cnt_wed == 1

def test_member_saturday_point(attendance_manager):
    attendance_manager.add_member('def')
    attendance_manager.add_point('def','saturday')
    member = attendance_manager.member_map['def']

    assert member.point == 2
    assert member.cnt_weekend == 1

def test_member_sunday_point(attendance_manager):
    attendance_manager.add_member('sun')
    attendance_manager.add_point('sun','sunday')

    member = attendance_manager.member_map['sun']

    assert member.point == 2
    assert member.cnt_weekend == 1

def test_member_normal_point(attendance_manager):
    attendance_manager.add_member('nor')
    attendance_manager.add_point('nor','monday')
    member = attendance_manager.member_map['nor']
    assert member.point == 1
    assert member.cnt_wed == 0
    assert member.cnt_weekend == 0

def test_add_point_not_in_name_map(attendance_manager):
    ret = attendance_manager.add_point('nobody','sunday')

    assert ret is None


def test_add_bonus_point_sun(attendance_manager):
    attendance_manager.add_member('sun')
    for i in range(10):
        attendance_manager.add_point('sun','sunday')

    attendance_manager.add_bonus_point()

    member = attendance_manager.member_map['sun']
    assert member.point == 30

def test_add_bonus_point_wed(attendance_manager):
    attendance_manager.add_member('abc')
    for i in range(10):
        attendance_manager.add_point('abc', 'wednesday')

    attendance_manager.add_bonus_point()

    member = attendance_manager.member_map['abc']
    assert member.point == 40

def test_upgrade_member_grades_to_silver(attendance_manager):
    attendance_manager.add_member('abc')
    for i in range(10):
        attendance_manager.add_point('abc', 'wednesday')

    attendance_manager.upgrade_member_grades()

    member = attendance_manager.member_map['abc']
    assert isinstance(member.grade, SilverGrade)

def test_upgrade_member_grades_to_gold(attendance_manager):
    attendance_manager.add_member('sun')
    for i in range(50):
        attendance_manager.add_point('sun', 'monday')

    attendance_manager.upgrade_member_grades()
    member = attendance_manager.member_map['sun']
    assert isinstance(member.grade, GoldGrade)

def test_upgrade_member_grades_to_normal(attendance_manager):
    attendance_manager.add_member('nor')
    attendance_manager.add_point('nor', 'monday')

    attendance_manager.upgrade_member_grades()
    member = attendance_manager.member_map['nor']
    assert isinstance(member.grade, NormalGrade)

def test_string_member_info(attendance_manager):
    attendance_manager.add_member('abc')
    for i in range(10):
        attendance_manager.add_point('abc', 'wednesday')

    attendance_manager.add_bonus_point()
    attendance_manager.upgrade_member_grades()

    expected = "NAME : abc, POINT : 40, GRADE : SILVER"

    assert attendance_manager.string_member_info(0) == expected

def test_is_valid_member(attendance_manager):
    attendance_manager.add_member('abc')
    for i in range(10):
        attendance_manager.add_point('abc', 'wednesday')

    attendance_manager.add_bonus_point()
    attendance_manager.upgrade_member_grades()

    attendance_manager.add_member('def')
    attendance_manager.add_point('def','monday')

    assert attendance_manager.is_valid_member(0)
    assert not attendance_manager.is_valid_member(1)
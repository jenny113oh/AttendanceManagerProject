import pytest

from member import Member
from member_grade import NormalGrade, SilverGrade


@pytest.fixture
def member():
    return Member('TEST',100)

def test_member(member):
    assert member.name == 'TEST'
    assert member.id == 100
    assert member.point == 0
    assert isinstance(member.grade,NormalGrade)
    assert member.cnt_wed == 0
    assert member.cnt_weekend == 0

def test_member_name(member):
    member.name = 'JEN'
    assert member.name == 'JEN'

def test_member_id(member):
    member.id = 1
    assert member.id == 1

def test_add_points(member):
    org_point = member.point

    member.add_point(10)
    assert member.point == org_point + 10

def test_member_grade(member):
    member.grade = SilverGrade()
    assert isinstance(member.grade, SilverGrade)

def test_add_cnt_weds(member):
    org_cnt_wed = member.cnt_wed

    member.add_cnt_wed()
    assert member.cnt_wed == org_cnt_wed + 1

def test_add_cnt_weekend(member):
    org_cnt_weekend = member.cnt_weekend
    member.add_cnt_weekend()
    assert member.cnt_weekend == org_cnt_weekend + 1


import pytest
import sys
import io
from print_manager import PrintManager
from attendancemanager import AttendanceManager

output = io.StringIO()
sys.stdout = output

@pytest.fixture
def print_manager():
    return PrintManager()

@pytest.fixture
def attendance_manager():
    attendance_manager = AttendanceManager()
    attendance_manager.add_member('abc')
    attendance_manager.add_point('abc','monday')
    attendance_manager.add_bonus_point()
    attendance_manager.upgrade_member_grades()

    return attendance_manager

def test_print_attendance(attendance_manager, print_manager):
    output.seek(0)
    output.truncate(0)
    expected = "NAME : abc, POINT : 1, GRADE : NORMAL\n"
    print_manager.print_attendance(attendance_manager)

    assert output.getvalue() == expected

def test_print_removed_members(attendance_manager,print_manager):
    output.seek(0)
    output.truncate(0)
    expected = '\nRemoved player\n==============\nabc\n'
    print_manager.print_removed_members(attendance_manager)

    assert output.getvalue() == expected

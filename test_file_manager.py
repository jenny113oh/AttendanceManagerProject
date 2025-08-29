import pytest
import sys
import io

from attendancemanager import AttendanceManager
from file_manager import FileManager

@pytest.fixture
def file_manager():
    return FileManager()

@pytest.fixture
def attendance_manager():
    return AttendanceManager()


output = io.StringIO()
sys.stdout = output

def test_read_attendance_file(file_manager, attendance_manager):
    file_manager.read_attendance_file(attendance_manager,'attendance_weekday_500.txt')

    assert attendance_manager.member_cnt() == 19

def test_read_attendance_non_file(file_manager, attendance_manager):
    output.seek(0)
    output.truncate(0)

    file_manager.read_attendance_file(attendance_manager,'attendance_non.txt')


def test_read_attendance_not_split_2(file_manager, attendance_manager, mocker):
    mocker.patch('builtins.open', mocker.mock_open(read_data='Hello'))

    file_manager.read_attendance_file(attendance_manager,'attendance.txt')

    assert attendance_manager.member_cnt() == 0
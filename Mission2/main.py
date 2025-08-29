from attendancemanager import AttendanceManager
from file_manager import FileManager
from print_manager import PrintManager

if __name__ == '__main__':
    attendance_manager = AttendanceManager()
    file_manager = FileManager()
    print_manager = PrintManager()

    file_manager.read_attendance_file(attendance_manager,'attendance_weekday_500.txt')
    print_manager.print_attendance(attendance_manager)
    print_manager.print_removed_members(attendance_manager)

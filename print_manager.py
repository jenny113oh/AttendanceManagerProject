from attendancemanager import AttendanceManager


class PrintManager:

    def print_attendance(self, attendance_manager:AttendanceManager):
        for i in range(attendance_manager.member_cnt()):
            print(attendance_manager.string_member_info(i))

    def print_removed_members(self, attendance_manager:AttendanceManager):
        print("\nRemoved player")
        print("==============")
        for i in range(attendance_manager.member_cnt()):
            if not attendance_manager.is_valid_member(i):
                print(attendance_manager.member_name(i))
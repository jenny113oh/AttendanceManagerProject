from attendancemanager import AttendanceManager


class FileManager:
    def read_attendance_file(self, attendance_manager:AttendanceManager, file_name: str):
        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                for line in f.readlines():
                    attendance_weekday = line.strip().split()
                    if len(attendance_weekday) != 2:
                        continue
                    attendance_manager.add_member(attendance_weekday[0])
                    attendance_manager.add_point(attendance_weekday[0], attendance_weekday[1])

                attendance_manager.add_bonus_point()
                attendance_manager.upgrade_member_grades()
            return
        except FileNotFoundError:
            print("파일을 찾을 수 없습니다.")
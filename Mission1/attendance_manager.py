member_name_to_num_map = {}
id_cnt = 0

member_points = [0] * 100
member_grade = [''] * 100
member_name_list = [''] * 100
count_wed = [0] * 100
count_weekend = [0] * 100

def add_member(member_name: str):
    global id_cnt

    if member_name in member_name_to_num_map:
        return

    id_cnt += 1
    member_name_to_num_map[member_name] = id_cnt
    member_name_list[id_cnt] = member_name
    return

def add_point(member_name: str, attend_day : str):
    member_id = member_name_to_num_map.get(member_name,0)
    if member_id == '0':
        return

    if attend_day == "wednesday":
        member_points[member_id] += 3
        count_wed[member_id] += 1
    elif attend_day == "saturday" or attend_day == "sunday":
        member_points[member_id] += 2
        count_weekend[member_id] += 1
    else :
        member_points[member_id] += 1
    return

def read_attendance_file():
    try:
        with open('attendance_weekday_500.txt', 'r', encoding='utf-8') as f:
            for line in f.readlines():
                attendance_weekday = line.strip().split()
                if len(attendance_weekday) != 2:
                    continue
                add_member(attendance_weekday[0])
                add_point(attendance_weekday[0], attendance_weekday[1])
        return
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")

def add_bonus_points():
    for i in range(1, id_cnt + 1) :
        if count_wed[i] > 9 :
            member_points[i] += 10
        if count_weekend[i] > 9:
            member_points[i] += 10

def check_member_grades():
    for i in range(1, id_cnt + 1) :
        if member_points[i] >= 50:
            member_grade[i] = 'GOLD'
        elif member_points[i] >= 30:
            member_grade[i] = 'SILVER'
        else:
            member_grade[i] = 'NORMAL'

def print_member_name_and_grade():
    for i in range(1, id_cnt + 1) :
        print(f"NAME : {member_name_list[i]}, POINT : {member_points[i]}, GRADE : {member_grade[i]}")

def print_removed_members():
    print("\nRemoved player")
    print("==============")
    for i in range(1, id_cnt + 1):
        if member_grade[i] == 'NORMAL' and count_wed[i] == 0 and count_weekend[i] == 0:
            print(member_name_list[i])


if __name__ == "__main__":
    read_attendance_file()
    add_bonus_points()
    check_member_grades()
    print_member_name_and_grade()
    print_removed_members()

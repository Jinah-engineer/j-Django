absent = [2, 5] # 결석
no_book = [7]
for student in range(1, 11): #1, 2, 3, 4....10
    if student in absent: # 학생이 list 안에 포함되어있는 경우
        continue
    elif student in no_book:
        print('오늘 수업 여기까지. {0}는 교무실로 따라와'.format(student))
        break
    print("{0}, 책을 읽어보아.".format(student))



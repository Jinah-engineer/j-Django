print('python', 'java', sep=" vs ")  # separator

# 한 줄에 출력
# end : 문장의 끝 부분을 ---로 바꾼다 (한 문장으로 출력)
print('python', 'java', sep=",", end="?")  # separator
print('무엇이 더 재밌을까요?')

import sys
# stdout = 표준 출력
# print("python", "java", file=sys.stdout)

# stderr = 표준 에러
# print("python", "java", file=sys.stderr)

print('----------------------------------')
scores = {'수학':0, '영어':50, '코딩':100}
for subject, score in scores.items():
     # print(subject, score)
     # ljust = 왼쪽 정렬, rjust = 오른쪽 정렬
     # 8글자 만큼 떨어져서 왼쪽 정렬
    print(subject.ljust(8), str(score).rjust(4), sep=":")

print('----------------------------------')

# 은행 대기 순번표
# 001, 002, 003, ...
for num in range(1, 21):
    # zfill : 3크기 만큼 공간을 확보하고 값을 넣는데, 값이 없는 부분은 0으로 채운다.
    print("대기번호 :" + str(num).zfill(3))

print('----------------------------------')

answer = input('아무 값이나 입력하세요 : ')
print(type(answer))
print('입력하신 값은 ' + answer + '입니다.')

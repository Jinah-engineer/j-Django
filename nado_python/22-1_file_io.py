# w = write (쓰기 위한 목적)
score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
# 반드시 close 해주기
score_file.close()

# a = append --> 줄바꿈이 되지 않기 때문에 줄바꿈을 추가해줘야 함
score_file = open('score.txt', 'a', encoding='utf8')
score_file.write('과학 : 80')
score_file.write('\n코딩 : 100')
score_file.close()

# r = read -> console 에 출력
score_file = open('score.txt', 'r', encoding='utf8')
print(score_file.read())
score_file.close()

score_file = open('score.txt', 'r', encoding='utf8')
print(score_file.readline(), end="")  # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()

print('\n')
print('------------------------------------')

# while 문을 통해 처리
score_file = open('score.txt', 'r', encoding='utf8')
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

print('\n')
print('------------------------------------')

# list 형태로 저장
score_file = open('score.txt', 'r', encoding='utf8')
lines = score_file.readlines()
for line in lines:
    print(line, end="")
score_file.close()
# 문자 개수 세기 (count)
a = 'hobby'
print(a.count('b')) # 문자 b의 개수

# 위치 알려주기 1 (find)
a = 'Python is the best choice'
print(a.find('b')) # 문자열에서 b가 처음 나온 위치
print(a.find('k')) # 찾는 문자 or 문자열이 존재하지 않는다면 -1을 반환한다

# 위치 알려주기 2 (index)
a = 'Life is too short'
print(a.index('t')) # 문자 t가 맨 처음으로 나온 위치 반환
# print(a.index('k')) -- 찾는 문자 or 문자열이 존재하지 않으면 오류 발생

# 문자열 삽입 (join)
print(",".join('abcd')) # 문자열, 리스트, 튜플도 입력으로 사용할 수 있다
print(",".join(['a', 'b', 'c', 'd']))

# 소문자로 대문자로 바꾸기 (upper)
a = "hi"
print(a.upper())

# 대문자를 소문자로 바꾸기 (lower)
a = "HI"
print(a.lower())

# 왼쪽 공백 지우기 (lstrip)
a = " hi "
print(a.lstrip())

# 오른쪽 공백 지우기 (rstrip)
a = " hi "
print(a.rstrip())

# 문자열 바꾸기 (replace)
a = "Life is too short"
print(a.replace("Life", "Your leg"))

# 문자열 나누기 (split)
a = "Life is too shoft"
print(a.split()) # 공백을 기준으로 문자열 나눔

b = "a:b:c:d"
print(b.split(':')) # : 기호를 기준으로 문자열 나눔



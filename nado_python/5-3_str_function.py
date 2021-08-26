python = 'Python is Amazing'

# lowercase
print(python.lower())

# upppercase
print(python.upper())

# optional uppercase - boolean
print(python[0].isupper())

# 길이
print(len(python))

# replace
print(python.replace('Python','Java'))

# n이라는 글자의 index
index = python.index("n")
print(index)

# start 위치(=index) 이후(=index가 6)에 존재하는 n을 찾는다
index = python.index('n', index+1)
print(index)

# n이 있는 index
print(python.find("n"))

# 내가 원하는 값을 포함하지 않을 경우에는 -1 반환
print(python.find('Java'))

# 하지만 index 함수의 경우 존재하지 않는 값을 넣으면 error를 발생시키며 프로그램이 종료된다
# print(python.index('Java'))

# error 이후의 코드는 실행되지 않는다.
print('hi')

# 값의 개수
print(python.count('n'))
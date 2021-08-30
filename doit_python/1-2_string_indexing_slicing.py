# indexing : 무언인가를 '가리킨다'
# slicing : 무엇인가를 '잘라낸다'

# String indexing
a = "Life is too short, you need Python"
print(a[3])
print(a[-2]) # 뒤에서 2번째 문자
print(a[-5]) # 뒤에서 5번째 문자


# String Slicing
print(a[0:4])

# [시작번호:] = 시작번호부터 그 문자열의 끝까지
print(a[19:])

# [:끝번호] = 문자열의 처음부터 끝 번호까지
print(a[:17])

# [ : ] = 문자열의 처음부터 끝가지
print(a[:])

print(a[19:-7])

print('-' * 50)

# Slicing Example
a = '20010331Rainy'
year = a[:4]
day = a[4:8]
weather = a[8:]
print(year)
print(day)
print(weather)

print('-' * 50)

# ex2
a = 'Pithon'
print(a[1])
print(a[:1] + 'y' + a[2:])
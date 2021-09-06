# 숫자 바로 대입
print('I eat {0} apples.'.format(3))

# 문자열 바로 대입하기
print('I eat {0} apples.'.format("five"))

# 숫자 값을 가진 변수로 대입하기
number = 3
print('I eat {0} apples.'.format(number))

# 2개 이상의 값 넣기
number = 10
day = 'three'
print('I ate {0} apples. so I was sick for {1} days.' .format(number, day))

# 이름으로 넣기 name = value
print('I ate {number} apples. so I was sick for {day} days.'.format(number=10, day=3))

# index 와 name 을 혼용해서 넣기
print('I ate {0} apples. so I was sick for {day} days.'.format(10, day=3))

print('=' * 50)

# 왼쪽 정렬 + 문자열의 총 자릿수 10개 한정
print('{0:<10}'.format('left'))

# 오른쪽 정렬 + 문자열 총 자릿수 10개
print('{0:>10}'.format('right'))

# 가운데 정렬
print('{0:^10}'.format('center'))

# 공백 채우기
print('{0:=^10}'.format('empty'))

# !
print('{0:!<10}'.format('oh'))

print('=' * 50)

# 소수점 표현하기 - 소수점 4자리까지만 표시
y = 3.42143423
print('{0:0.4f}'.format(y))

print('{0:10.4f}'.format(y))

# 문자 표현하기
print('{{ and }}'.format())




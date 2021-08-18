print('a' + 'b')
print('a', 'b')

# tip 1
print('나는 %d살입니다.' %20) # d = decimal = 정수
print('나는 %s을 좋아해요.' %'파이썬') # s = string = 문자열
print('Apple은 %c로 시작해요.' %'A') # c = character = 문자

print('나는 %s살입니다.' %20)
print('나는 %s색과 %s색을 좋아해요' %('파란', '빨간'))

# tip 2
print('나는 {}살입니다.' .format(20))
print('나는 {}색과 {}색을 좋아해요.' .format('파란', '빨간'))

print('나는 {0}색과 {1}색을 좋아해요.' .format('파란', '빨간')) # format의 값을 index로 인식 가능
print('나는 {1}색과 {0}색을 좋아해요.' .format('파란', '빨간')) # format의 값을 index로 인식 가능

# tip 3
print('나는 {age}살이며, {color}색을 좋아해요.' .format(age = 20, color = '빨간')) # 변수 사용

# tip 4
age = 20
color = '빨간'
print(f'나는 {age}살이며, {color}색을 좋아해요.') # f를 사용하여 전역 변수를 넣어줄 수 있다.
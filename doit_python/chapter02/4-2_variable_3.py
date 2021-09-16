# 변수를 만드는 여러가지 방법
a, b = ('python', 'life')
(a, b) = 'python', 'life'
print(a, b) # 튜플은 괄호 생략 가능

# list
[a, b] = ['python', 'life']
print([a, b])

# multiple values
a = b = 'python'
print(a)
print(b)

print('='*30)

# 두 변수 값 바꾸기
a = 3
b = 5
a, b = b, a
print(a)
print(b)



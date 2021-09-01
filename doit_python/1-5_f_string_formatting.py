# prefix 'f'
# f 문자열 포매팅 -> 변수 값을 생성한 후에 그 값을 참조할 수 있다.
name = '박진아'
age = 27
print(f'나이 이름은 {name}입니다. 나이는 {age}입니다.' )
print(f'나는 내년이면 {age + 1}살이 된다.')

# dictionary 사용 (** dictionary : key 와 value 라는 것을 한 쌍으로 갖는 자료형)
d = { 'name' : '박진아', 'age' : 27}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')

print('=' * 50)

# 정렬
print(f'{"hi":<10}', '왼쪽 정렬')
print(f'{"hi":>10}', '오른쪽 정렬')
print(f'{"hi":^10}', '가운데 정렬')

# 공백 채우기
print(f'{"hi":=^10}', ': 가운데 정렬하고 = 문자로 공백 채우기')
print(f'{"hi":!<10}', ': 왼쪽 정렬하고 ! 문자로 공백 채우기')

print('=' * 50)

# 소수점 4자리까지만 표현
y = 3.42132324
print(f'{y:0.4f}')

# 소수점 4자리까지 표현하고 총 자릿수를 10으로 맞춤
print(f'{y:10.4f}')

# {} 문자 표현
print(f'{{ and }}')



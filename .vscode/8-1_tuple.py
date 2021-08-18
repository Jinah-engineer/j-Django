# Tuple
# list 보다 속도가 빠름. 내용 변경이나 추가는 어려움. 변경되지 않는 목록을 사용할 때 활용 가능하다.
menu = ('돈까스', '치즈돈까스')
print(menu[0])
print(menu[1])

name = '박진아'
age = 27
hobby = '코딩'
print(name, age, hobby)

(name, age, hobby) = ('박진아', 27, '코딩')
print(name, age, hobby)

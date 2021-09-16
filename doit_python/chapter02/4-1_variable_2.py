# b 변수를 생성할 때, a 변수의 값을 가져오면서 a 와는 다른 주소를 가리키도록 만드는 방법

# [:] 사용하기
a = [1, 2, 3]

b = a[:] # 리스트 a 의 처음 요소부터 끝 요소까지 슬라이싱

a[1] = 4
print(a)
print(b)


# copy 모듈 사용
from copy import copy
a = [1, 2, 3]
b = copy(a)
print(b)
print(b is a) # b와 a가 가리키는 객체는 서로 다르다





print('='*20, 'filter', '='*20)
'''
    9. filter : 1번째 인수로 함수 이름을, 2번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형을 받는다.
                그리고 2번째 인수인 반복 가능한 자료형 요소가 1번째 인수인 함수에 입력되었을 때,
                반환 값이 참인 것만 묶어서(걸러 내서) 돌려준다. 
'''

def positive(l):
    result = [] # 반환 값이 참인 것만 filter 해서 저장할 변수
    for i in l:
        if i > 0: # i 가 0보다 클 때
            result.append(i) # 리스트에 i 추가
    return result

print(positive([1, -3, 2, 0, -5, 6]))

# 필터로 바꾸면
def positive_filter(x):
    return x > 0

print(list(filter(positive_filter, [1, -3, 2, 0, -5 , 6])))

# 람다 사용
print(list(filter(lambda x: x > 0, [1, -3, 2, 0, -5 ,6])))


print('='*20, 'hex', '='*20)
'''
    10. hex : 정수 값을 입력받아 16진수(hexadecimal)로 변환하여 돌려준다
'''
print(hex(234))
print(hex(3))


print('='*20, 'id', '='*20)
'''
    11. id : 객체를 입력받아 객체의 고유 주소 값(reference)을 돌려주는 함수
'''
a = 3
b = a
print(id(3))
print(id(a))
print(id(b))


print('='*20, 'input', '='*20)
'''
    12. input : 사용자 입력을 받는 함수
'''
# b = input('Enter: ')


print('='*20, 'int', '='*20)
'''
    13. int : 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 돌려준다
'''
print(int('3'))
print(int(3.4))
print(int('11', 2)) # 2진수로 표현된 11의 10진수 값
print(int('1A', 16)) # 16진수로 표현된 1A의 10진수 값


print('='*20, 'isinstance', '='*20)
'''
    14. isinstance : 1번째 인수로 instance, 2번째 인수로 class 이름을 받는다.
                     입력받은 instance 가 그 class 의 instance 인지를 판단여
                     참이면 True, 거짓이면 False 
'''
class Person: pass # 아무 기능이 없는 Person 클래스 생성
a = Person() # Person 클래스의 인스턴스 a 생성
print(isinstance(a, Person))











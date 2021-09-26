# 계산기
'''
    클래스가 필요한 이유
'''
'''
    1. class 가 없을 때
'''
print('='*20, 'example 01', '='*20)

result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add1(5))
print(add1(7))

print('='*20, 'example 02 - class', '='*20)

'''
    2. class 를 사용할 때
'''

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(5))
print(cal2.add(7))
print(cal2.sub(5))

'''
    클래스와 객체
        - 과자 틀  = 클래스(class)
        - 과자 틀을 사용해 만든 과자 = 객체(object)
        - 동일한 클래스로 만든 객체들은 서로 전혀 영향을 주지 않는다
        - 1개의 클래스는 무수히 많은 객체를 만들어 낼 수 있다
        
        
    객체와 인스턴스의 차이 
        - a = Cookie()
        - 여기서 a 는 객체
        - a 객체는 Cookie 의 인스턴스
        - 인스턴스 : 특정 객체(a)가 어떤 클래스(Cookie)의 객체인지를 관계 위주로 설명할 때 사용한다
'''
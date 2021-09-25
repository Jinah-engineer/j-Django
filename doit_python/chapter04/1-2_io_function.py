"""
    입력값과 결과값에 따른 함수의 형태
"""
"""
    1. 일반적인 함수 
        def 함수 이름(매개변수):
            수행할 문장
            ...
            return 결과값
            
        결과값을 받을 변수 = 함수이름(입력인수 1, 입력인수 2, ...) 
"""
def add(a, b):
    result = a + b
    return result

a = add(3, 4)
print(a)

"""
    2. 입력값이 없는 함수 
     
        결과값을 받을 변수 = 함수 이름()
"""
def say():
    return 'Hi'
a = say()
print(a)

"""
    3. 결과값이 없는 함수
    
         함수 이름(입력인수1, 입력인수2, ...)
"""
def add(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))

"""
    4. 입력값도 결과값도 없는 함수
    
        함수 이름()
"""
def say():
    print('Hi')
say()

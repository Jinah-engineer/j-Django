'''
    Don't Reinvent the wheel! 이미 있는 것을 다시 만드느라 쓸데없이 시간을 낭비하지 말라.

    파이썬 내장함수는 외부 모듈과 달리,
    import 가 필요하지 않기 때문에 아무런 설정 없이 바로 사용할 수 있다.
'''

print('='*20, 'abs', '='*20)
'''
    1. abs : 어떤 숫자를 입력받았을 때 그 숫자의 절대값을 돌려준다
'''
print(abs(3))
print(abs(-3))
print(abs(-1.2))

print('='*20, 'all', '='*20)
'''
    2. all : 반복 가능한(iterable) 자료형 x 를 입력 인수로 받으며,
             이 x 가 모두 참이면 True, 
             거짓이 하나라도 있으면 False 를 돌려준다.
'''
print(all([1, 2, 3, 0])) # 0은 거짓


print('='*20, 'any', '='*20)
'''
    3. any : x 중 하나라도 참이 있으면 True,
             x 가 모두 거짓일 때에만 False 를 돌려준다.
             all(x) 의 반대
'''
print(any([1, 2, 3, 0]))
print(any([0, ""]))


print('='*20, 'chr', '='*20)
'''
    4. chr : 아스키(ASCII) 코드 값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수
'''
print(chr(97))
print(chr(48))


print('='*20, 'dir', '='*20)
'''
    5. dir : 객체가 자체적으로 가지고 있는 변수나 함수를 보여준다
'''
print(dir([1, 2, 3])) # list 객체 관련 함수
print(dir({'1':'a'})) # dictionary 객체 관련 함수


print('='*20, 'divmod', '='*20)
'''
    6. divmod : 2개의 숫자를 입력으로 받는다. 그리고 a 를 b 로 나눈 몫과 나머지를 튜플 형태로 돌려준다
'''
print(divmod(7, 3)) # 7 나누기 3의 몫은 2, 나머지는 1
print(7 // 3)
print(7 % 3)


print('='*20, 'enumerate', '='*20)
'''
    7. enumerate : '열거하다'. 순서가 있는 자료형(list, tuple, string)을 입력으로 받아 
                   index 값을 포함하는 enumerate 객체를 돌려준다 
'''
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

# for 문 처럼 반복되는 구간에서 객체가 현재 어느 위치에 있는지 알려주는 index 값이 필요할 때 유용하다


print('='*20, 'eval', '='*20)
'''
    8. eval : 실행 가능한 문자열(1+2, 'hi' + 'a' 같은 것)을 입력으로 받아
              문자열을 실행한 결과값을 돌려준다 
              
              입력받은 문자열로 파이썬 함수나 클래스를 동적으로 실행하고 싶을 때 사용한다
'''
print(eval('1+2'))
print(eval("'hi'+'a'"))
print(eval('divmod(4,3)'))





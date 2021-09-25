# 함수 안에서 선언한 변수의 효력 범위
"""
    local vs. global?
"""
'''
    1. 함수 안에서 함수 밖의 변수를 변경하는 방법
    
        1) return 사용하기
'''
a = 1
def vartest(a):
    a = a + 1
    return a

a = vartest(a)
print(a)
'''
        2) global 명령어 사용하기
            ** 하지만 프로그래밍을 할 때 global 명령어는 사용하지 않는 것이 좋다. 
               왜냐하면 함수는 독립적으로 존재하는 것이 좋기 때문이다!
'''
b = 1
def vartest2():
    global b
    b = b + 2
vartest2()
print(b)


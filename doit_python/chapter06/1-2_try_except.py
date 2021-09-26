'''
    오류 예외 처리 기법
'''
'''
    1. try, except statement
    
        try: 
        ...
        except [발생 오류[as 오류 메시지 변수]]: --- 괄호 안의 내용은 생략 가능
        ...
'''
'''
    1) try, except 만 쓰는 방법
        : 오류 종류에 상관없이 오류가 발생하면 except 블록을 수행한다
'''
try:
    pass
except:
    pass

'''
    2) 발생 오류만 포함한 except 문
        : 오류가 발생했을 때 except 문에 미리 정해 놓은 오류 이름과 일치할 때만 except 블록을 수행한다
'''
try:
    pass
except ZeroDivisionError:
    pass

'''
    3) 발생 오류와 오류 메시지 변수까지 포함한 except 문
        : 오류 메시지의 내용까지 알고 싶을 때 사용하는 방법
'''
try:
    4 / 0
except ZeroDivisionError as e:
    print(e)
    # 출력 : division by zero



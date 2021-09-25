# 매개변수에 초기값 미리 설정하기
def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("응용이", 27)
say_myself("응용이2", 27, False)

"""
    주의해야 할 점 : 초기값을 설정할 때의 매개변수 위치는 항상 뒤쪽에 놓자
"""
'''
    def say_myself(name, man=True, old):
     print("나의 이름은 %s입니다." % name)
     print("나이는 %d살이빈다." % old)
     if man:
        print("남자입니다")
     else:
        print("여자입니다.")
        
    SyntaxError : non-default argument follows default argument
'''
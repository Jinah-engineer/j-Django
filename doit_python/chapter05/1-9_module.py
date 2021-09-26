'''
    모듈
'''
'''
    모듈 : 함수 or 변수 or 클래스를 모아 놓은 파일
    
    - 다른 파이썬 프로그램에서 불러와 사용할 수 있게끔 만든 파이썬 파일이라고도 할 수 있다
'''

print('='*20, '모듈 만들기', '='*20)
# 모듈 만들기 - mod1.py

print('='*20, '모듈 불러오기', '='*20)
# 모듈 불러오기
import mod1
print(mod1.add(3, 4))
print(mod1.sub(4, 2))



print('='*20, '모듈 사용하기', '='*20)
'''
    모듈 이름 없이 함수 이름만 쓰고 싶을 때
    
    from 모듈이름 import 모듈함수
        - from mod1 import add, sub
        - from mod1 import *
'''
from mod1 import add
print(add(3, 4))







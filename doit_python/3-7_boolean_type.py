"""
    bool type : True or False
"""
a = True
b = False

print(type(a))
print(type(b))

print(1 == 1)
print(2 > 1)
print(1 > 2)

print('='*10, '자료형의 참과 거짓','='*10)
"""
    String 
        1. "python" = True
        2. "" = False
    
    List
        1. [1, 2, 3] = True
        2. [] = False
        
    Tuple
        1. () = False
    
    Dictionary
        1. {} = False
    
    Decimal 
        1. 0이 아닌 숫자 = True
        2. 0 = False
        3. None = False
"""

print('='*10, 'example','='*10)
a = [1, 2, 3, 4]
while a:
    a.pop()
print(a)    # 빈 리스트로 변경되어 거짓 >> while 문의 조건이 거짓이 되므로 중지





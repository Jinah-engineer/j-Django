"""
     and or not
"""
"""
    x or y : x 와 y 둘 중에 하나만 참이어도 참
    x and y : x 와 y 모두 참이어야 참이다
    not x : x 가 거짓이면 참이다
"""

money = 2000
card = True
if money >= 3000 or card:
    print('택시를 타고 가라.')
else:
    print('걸어가라.')

print('='*30)


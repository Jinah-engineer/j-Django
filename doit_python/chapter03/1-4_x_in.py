"""
    x in list <--> x not in list
    x in tuple <--> x not in tuple
    x in string <--> x not in string
"""

print('='*20 + 'x in list' + '='*20)

print(1 in [1, 2, 3]) # 1이 [1, 2, 3] 안에 있는가
print(1 not in [1, 2, 3]) # 1이 [1, 2, 3,] 안에 없는가

print('='*20 + 'x in tuple' + '='*20)

print('a' in ('a', 'b', 'c'))
print('j' not in ('python'))

print('='*20 + 'x in list - example' + '='*20)

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print('take a taxi, please.')
else:
    print('just walk, please.')

print('='*20 + 'x in list - example 02' + '='*20)

# 주머니에 돈이 있으면 가만히 있고, 주머니에 돈이 없으면 카드를 꺼내라.
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print('take out a card')






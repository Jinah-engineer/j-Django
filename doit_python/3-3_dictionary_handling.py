# 딕셔너리에서 Key 사용해 Value 얻기
grade = {'pey': 10, 'julliet': 99}
print(grade['pey']) # Key가 'pey'인 딕셔너리의 Value를 반환
print(grade['julliet'])

# a[x] 에서 x는 Key에 해당하는 숫자를 가리킨다 --- 리스트, 튜플과는 다르다
a = {'a':1, 'b':2}
print(a['a'])
print(a['b'])

print('='*50)
dic = {'name':'pey', 'phone':'01232323', 'birth':'1128'}
print(dic['name'])
print(dic['phone'])
print(dic['birth'])

# 딕셔너리를 만들 때 주의할 사항
"""
    - Key 는 고유한 값이므로 중복되는 Key 값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시된다
    동일한 Key 가 존재하면 어떤 Key 에 해당하는 Value 를 불러야 할 지 알 수 없기 때문이다
    
    - Key 에 리스트는 쓸 수 없다. 
    - 하지만 tuple 은 Key 로 쓸 수 있다.
    
    - 딕셔너리의 Key 로 쓸 수 있느냐 없느냐는 Key 가 변하는 값인지 변하지 않는 값인지에 달려 있다.
    - 리스트는 그 값이 변할 수 있기 때문에 Key 로 쓸 수 없다. 
    
    - 딕셔너리의 Key 값으로 딕셔너리는 사용할 수 없다. 
"""
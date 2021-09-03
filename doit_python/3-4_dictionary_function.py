# Key 리스트 만들기 (keys)
a = {'name': 'pey', 'phone': '011232023', 'birth': '1118'}
print(a.keys())  # a 의 key 만을 모아서 dict_keys 객체를 돌려준다

for k in a.keys(): # for 문으로 key 객체 얻기
    print(k)

print(list(a.keys()))   # dict_keys 객체 리스트로 변환하기

print('='*50)

# Value 리스트 만들기 (values)
print(a.values())   # value 객체만 얻기

# Key, Value 쌍 얻기 (items)
print(a.items())

print('='*50)

# Key:Value 쌍 모두 지우기 (clear)
# print(a.clear())


# Key 로 Value 얻기 (get)
print(a.get('name'))
print(a.get('phone'))   # a['phone']을 사용했을 때와 동일한 결과값 리턴

"""
    하지만 만약 a['nokey']와 같이 존재하지 않는 키로 값을 가져오려 할 경우,
        1. a['nokey'] --> 오류 발생
        2. a.get('nokey') --> None 을 리턴한다
"""

# 미리 정해둔 default 값 가져오기 -- get(x, 'default value')
print(a.get('foo', 'bar'))

print('='*50)

# 해당 Key가 딕셔너리 안에 있는지 조사하기 (in)
print('name' in a)
print('email' in a)

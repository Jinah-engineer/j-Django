# key = 3 / value = '유재석'
cabinet = {3: '유재석', 100: '김태호'}

# key를 통해 value
print(cabinet[3])
print(cabinet[100])

# get method
print(cabinet.get(3))

# key가 존재하지 않으면 error
# print(cabinet[5])
print(cabinet.get(5)) # none (위 index key 접근과 결과 차이 있음)
print(cabinet.get(5, '사용 가능'))

# value의 존재여부 확인
print(3 in cabinet) # True
print(5 in cabinet) # False

# new example
cabinet = {'A-3' : '유재석', 'B-100' : '김태호'}
print(cabinet['A-3'])
print(cabinet['B-100'])

# 새 손님 - add, update
print(cabinet)
cabinet['A-3'] = '김종국'
cabinet['C-20'] = '조세호'
print(cabinet)

# 간 손님 - delete
del cabinet['A-3']
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)

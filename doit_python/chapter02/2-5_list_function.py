# 리스트에 요소 추가 (append)
a = [1, 2, 3]
a.append(4)
print(a)

a.append([5, 6]) # 리스트에 리스트를 추가
print(a)

# 리스트 정렬 (sort)
a = [1, 4, 3, 2]
a.sort()
print(a)

print('=' * 50)

a = ['a', 'c', 'b']
a.sort()
print(a)

# 리스트 뒤집기 (reverse)
a = ['a', 'c', 'b']
a.reverse() # 리스트를 역순으로 정렬하는 것이 아니라, 역순으로 뒤집어 준다
print(a)

# 위치 반환 (index) : x의 위치 값을 돌려준다
a = [1, 2, 3]
print(a.index(3))

# print(a.index(0)) -- 리스트에 존재하지 않는 값은 오류를 발생시킨다 (ValueError)

# 리스트에 요소 삽입 (insert)
a.insert(0, 4) # a[0] 위치에 4 삽입
print(a)

# 리스트 요소 제거 (remove) : 리스트에서 첫 번째로 나오는 x를 삭제하는 함수
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)

# 리스트 요소 끄집어내기 (pop) : 리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제하는 함수
a = [1, 2, 3]
a.pop()
print(a)

# 리스트에 포함된 요소 x 의 개수 세기 (count)
a = [1, 2, 3, 1]
print(a.count(1))

# 리스트 확장 (extend) : 원래의 리스트에 리스트 더하기
a = [1, 2, 3]
a.extend([4, 5])
print(a)

b = [6, 7]
a.extend(b)
print(a)


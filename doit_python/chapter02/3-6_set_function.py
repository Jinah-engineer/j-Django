
# 값 1개 추가하기 (add)
print('='*10, '값 1개 추가하기','='*10)

s1 = set([1, 2, 3])
s1.add(4)
print(s1)


# 값 여러 개 추가하기 (update)
print('='*10, '값 여러 개 추가하기','='*10)
s1.update([4, 5, 6])
print(s1)

# 특정 값 제거하기 (remove)
print('='*10, '특정 값 제거하기','='*10)
s1.remove(2)
print(s1)



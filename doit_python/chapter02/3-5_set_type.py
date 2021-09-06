# 집합 (set)
s1 = set([1, 2, 3])
print(s1)

s2 = set('Hello')
print(s2)

"""
    집합 자료형의 특징
        1. 중복을 허용하지 않는다.
        2. 순서가 없다. (Unordered) 
         ** 리스트와 튜플은 순서가 있다. (Ordered) 
            만약, set 자료형에 저장된 값을 indexing 으로 접근하려면 리스트나 튜플로 변환시켜야 한다. 
"""

print('='*10, 'set을 list, tuple로 변환','='*10)
l1 = list(s1)
print(l1)
t1 = tuple(s1)
print(t1)

print('='*10, '교집합, 차집합, 합집합','='*10)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# intersection
print('s1과 s2의 교집합은 {}입니다.'.format(s1 & s2))
print('s1과 s2의 교집합은 {}입니다.'.format(s1.intersection(s2)))


# union
print('s1과 s2의 합집합 {}입니다.'.format(s1 | s2))
print('s1과 s2의 합집합 {}입니다.'.format(s1.union(s2)))

# difference
print('s1과 s2의 차집합은 {}입니다.'.format(s1 - s2))
print('s1과 s2의 차집합은 {}입니다.'.format(s2 - s1))
print('s1과 s2의 차집합은 {}입니다.'.format(s1.difference(s2)))
print('s1과 s2의 차집합은 {}입니다.'.format(s2.difference(s1)))



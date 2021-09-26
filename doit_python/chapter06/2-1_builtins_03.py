print('='*20, 'len', '='*20)
'''
    15. len : 입력값 s 의 길이(요소 전체의 개수)를 돌려준다
'''
print(len('python'))
print(len([1, 2, 3]))
print(len((1, 'a')))


print('='*20, 'list', '='*20)
'''
    16. list : 반복 가능한 자료형 s 를 입력받아 리스트로 만들어 돌려준다
'''
print(list('python'))
print(list((1,2,3)))

# list 함수에 list 를 입력으로 주면 똑같은 list 를 복사하여 돌려준다
a = [1, 2, 3]
b = list(a)
print(b)


print('='*20, 'map', '='*20)
'''
    17. map : 함수와 반복 가능한(iterable) 자료형을 입력으로 받는다.
              map 은 입력 받은 자료형의 각 요소를 함수 f 가 수행한 결과를 묶어서 돌려준다
'''
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number * 2)
    return result

result = two_times([1, 2, 3, 4])
print(result)

# map 으로 변경하면
def two_times2(x):
    return x * 2

print(list(map(two_times2, [1, 2, 3, 4])))

# lambda 사용

print(list(map(lambda a : a * 2, [1, 2, 3, 4])))



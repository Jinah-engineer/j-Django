# list 내포 사용하기

"""
    [표현식 for 항목 in 반복 가능 객체 if 조건]

    for 문을 여러 개 사용할 때의 문법 :
        [표현식 for 항목1 in 반복 가능 객체1 if 조건1
                for 항목2 in 반복 가능 객체2 if 조건2
                    ...
                for 항목n in 반복 가능 객체n if 조건n]
"""

a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num * 3)

print(result)

# ****************
result = [num * 3 for num in a]
print(result)

result = [num * 3 for num in a if num % 2 == 0]
print(result)

print('='*30 + '구구단 결과 list 에 담기' + '='*30)
# 구구단 list 내포
result = [x * y for x in range(2, 10)
    for y in range(1, 10)]
print(result)

# 입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?
"""
    여러 개의 입력 값을 받는 함수 만들기
        *args 는 임의로 정한 변수 이름 (바꿔도 무방)
"""
def add_many(*args):
    result = 0
    for i in args:
        result = result + i # *args에 입력받은 모든 값을 더한다
    return result

result = add_many(1, 2, 3)
print(result)

result2 = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result2)



print('='*20, 'choice parameter', '='*20)

# choice parameter
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
        return result


result1 = add_mul('add', 1,2,3,4,5)
print(result1)

result2 = add_mul('mul', 1,2,3,4,5)
print(result2)


print('='*20, 'keyword parameter', '='*20)

# keyword parameter
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)

print_kwargs(name='foo', age=3)

# 모두 딕셔너리로 만들어져서 출력된다
# key = value

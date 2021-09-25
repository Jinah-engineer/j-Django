# 함수의 결과값은 언제나 하나이다
def add_and_mul(a,b):
    return a+b, a*b # return 1 tuple = (a+b, a*b)

result = add_and_mul(3,4)
print(result)

# tuple 값을 2개의 결과값처럼 받고 싶다면?
result1, result2 = add_and_mul(3, 4)
print(result1, result2)


# return 이 2개라면? 첫번째 return 만 실행된다!
def add_and_mul(a,b):
    return a+b
    return a*b

result = add_and_mul(2,3)
print(result)

"""
    특별한 상황일 때 함수를 빠져나가고 싶다면 return 을 단독으로 사용해서
    함수를 즉시 빠져나갈 수 있다
"""
def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s입니다." % nick)

say_nick("바보")
say_nick("야호")


"""
    lambda : 함수를 생성할 때 사용하는 예약어 (= def)

        - 함수를 한 줄로 간결하게 만들 때 사용한다
        - def 를 사용해야 할 정도로 복잡하지 않거나 def 를 사용할 수 없는 곳에 주로 쓰인다

    lambda 매개변수1, 매개변수2, ... : 매개변수를 사용한 표현식
"""

add = lambda a, b: a+b
result = add(3,4)
print(result)



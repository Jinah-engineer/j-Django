print('='*20, 'oct', '='*20)
'''
    18. oct : 정수 형태의 숫자를 8진수 문자열로 바꾸어 돌려준다
'''
print(oct(34))
print(oct(12345))


print('='*20, 'open', '='*20)
'''
    19. open : '파일 이름' 과 '읽기 방법' 을 입력받아 파일 객체를 돌려주는 함수
               읽기 방법(mode)을 생략하면 기본값인 읽기 전용 모드(r)로 파일 객체를 만들어 돌려준다
               
               w : 쓰기 모드
               r : 읽기 모드
               a : 추가 모드
               b : 바이너리 모드
'''


print('='*20, 'ord', '='*20)
'''
    20. ord : 문자의 아스키 코드 값을 돌려준다
'''
print(ord('a'))
print(ord('0'))


print('='*20, 'pow', '='*20)
'''
    21. pow : x 의 y 제곱한 결과값을 돌려준다
'''
print(pow(2, 4))
print(pow(3, 3))


print('='*20, 'range', '='*20)
'''
    22. range : 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 돌려준다
                for 문과 함께 자주 사용.
'''
# 인수가 하나일 경우 - 시작 숫자를 지정해주지 않으면 0부터 시작
print(list(range(5)))

# 인수가 2개일 경우 - 시작숫자, 끝 숫자. but 끝 숫자는 포함하지 않음
print(list(range(5, 10)))

# 인수가 3개일 경우 - 3번째 인수 = 숫자 사이의 거리
print(list(range(1, 10, 2)))
print(list(range(0, -10, -1)))


print('='*20, 'round', '='*20)
'''
    23. round : 숫자를 입력받아 반올림
'''
print(round(4.6))
print(round(4.2))
print(round(5.678, 2)) # 소수점 2자리까지만 반올림


print('='*20, 'sorted', '='*20)
'''
    24. sorted : 입력값을 정렬한 후 그 결과를 list 로 돌려준다 
                 주의할 점!
                 리스트 객체 그 자체를 정렬만 할 뿐, 정렬된 결과를 돌려주지 않는다
'''
print(sorted([3, 1, 2]))
print(sorted(['a', 'c', 'b']))
print(sorted("zero"))
print(sorted((3, 2, 1)))


print('='*20, 'str', '='*20)
'''
    25. str : 문자열 형태로 객체를 변환하여 돌려준다
'''
print(str(3))
print(str('hi'))
print(str('hi'.upper()))


print('='*20, 'sum', '='*20)
'''
    26. sum : 입력받은 list, tuple 의 모든 요소의 합을 돌려준다
'''
print(sum([1, 2, 3]))
print(sum((4, 5, 6)))


print('='*20, 'tuple', '='*20)
'''
    27. tuple : 반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 돌려준다
'''
print(tuple("abc"))
print(tuple([1, 2, 3]))
print(tuple((1, 2, 3)))


print('='*20, 'type', '='*20)
'''
    28. type : 입력값의 자료형이 무엇인지 알려준다
'''
print(type("abc"))
print(type([]))
print(type(open("test", 'w'))) # 파일 자료형


print('='*20, 'zip', '='*20)
'''
    29. zip : 동일한 개수로 이루어진 자료형을 묶어주는 역할.
'''
print(list(zip([1, 2, 3], [4, 5, 6])))
print(list(zip("abc", "def")))






# Insert int
print('I eat %d apples.' %3)

# Insert String
print('I eat %s apples.' %"five")

# Insert Variable
number = 3
print('I eat %d apples.' %number)

# Insert Multiple values
number = 10
day = "three"
print('I ate %d apples. so I was sick for %s days.' %(number, day))

# String format code
"""
    %s : 문자열(string)
    %c : 문자 1개(Character)
    %d : 정수 (Integer)
    %f : 부동 소수 (Floating-point)
    %o : 8진수
    %x : 16진수
    %% : Literal % (문자 '%' 자체)
"""

# %s : 어떤 형태의 값이든 변환해 넣을 수 있다 -> 자동으로 값을 문자열로 변환한다

# %%
print('Error is %d%%.' %98)

print('='*50)

# Format code와 숫자 함께 사용하기

# 1. 대입되는 값을 오른쪽으로 정렬 + 앞의 나머지는 공백
print('%10s' %'hi')

# 2. 왼쪽 정렬 + 나머지 공백
print('%-10sjane' %'hi')

# 3. 소수점 표현 (소수점 뒤에 나올 숫자의 개수)
print("%0.4f" %3.42132323)

# 4. 소수점 표시 + 오른쪽 정렬 + 공백
print("%10.4f" %3.4234234)


print('='*50)




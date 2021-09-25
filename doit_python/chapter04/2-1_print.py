# 숫자 출력
a = 123
print(a)

# 문자 출력
a = "Python"
print(a)

# list 출력
a = [1, 2, 3]
print(a)

'''
    1. 큰 따옴표(")로 둘러싸인 문자열은 + 연산과 동일하다
'''
print("life" "is" "too short")
print("life"+"is"+"too short")

'''
    2. 문자열 띄어쓰기는 콤마로 한다
'''
print("life", 'is', "too short")

'''
    3. 한 줄에 결과값 출력하기
'''
for i in range(10):
    print(i, end=' ') # 매개변수 end 를 이용해 끝 문자 지정 

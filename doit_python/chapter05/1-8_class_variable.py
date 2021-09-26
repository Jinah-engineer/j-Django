'''
    클래스 변수
'''
'''
    - 객체변수는 다른 객체들에 영향받지 않고 독립적으로 그 값을 유지한다.
    - 객체변수와 클래스 변수는 다르다!
'''

class Family:
    lastname = '김' # 클래스 변수

print(Family.lastname)

# Family 클래스로 만든 객체를 통해서도 클래스 변수를 사용할 수 있다
a = Family()
b = Family()

print(a.lastname)
print(b.lastname)

Family.lastname = '박'
print(a.lastname)
print(b.lastname)

'''
    클래스 변수값을 변경하면 >>> 클래스로 만든 객체의 lastname 값도 모두 변경된다. 
    즉, 클래스 변수는 클래스로 만든 모든 객체에 공유된다 ********
'''

print(id(Family.lastname))
print(id(a.lastname))
print(id(b.lastname))

# 3개 모두 같은 메모리를 가리킨다
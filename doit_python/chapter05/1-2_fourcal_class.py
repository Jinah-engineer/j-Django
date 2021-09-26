'''
    사칙연산 클래스 만들기
'''
'''
    1. 클래스를 어떻게 만들지 먼저 구상하기
        - setdata : 사칙연산을 하려면 두 숫자를 입력받아야겠군!
        - add : 더하기
        - div : 나누기
        - sub : 빼기
        - mul : 곱하기
'''
'''
    2. 클래스 구조 만들기
'''
class FourCal:
    pass

a = FourCal()
print(type(a)) # 객체 a 의 타입은 FourCal 클래스이다.

''' 
    3. 객체에 숫자 지정할 수 있게 만들기
'''
class FourCal:
    def setdata(self, first, second): # method 의 매개변수
        self.first = first # method 의 수행문 - 객체에 객체변수를 생성시킨다
        self.second = second

# self 의 경우 객체를 호출할 때 객체 자신이 전달되기 때문에 self 를 사용한 것이다

'''
    class 를 통해 method 를 호출하는 것도 가능하다
    :    '클래스 이름.메서드' 형태로 호출할 때는
         객체 a를 1번째 매개변수 self 에 꼭 전달해 주어야 한다
'''
a = FourCal()
FourCal.setdata(a, 4, 2)


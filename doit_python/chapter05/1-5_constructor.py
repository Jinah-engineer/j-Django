'''
    생성자 (constructor)
'''

'''
   만약 FourCal 클래스의 인스턴스 a 에 setdata 메서드를 수행하지 않고 add 메서드를 수행하면
   AttributeError: 'FourCal' object has no attribute 'first' 오류가 발생한다
   setdata 메서드를 수행해야 객체 a 의 객체변수 first 와 second 가 생성되기 때문이다 
   
   하지만 메서드를 호출하여 초기값을 설정하기 보다는 생성자를 구현하는 것이 안전한 방법이다. 
   
   생성자(constructor) : 객체가 생성될 때 자동으로 호출되는 메소드를 의미한다
   
   __init__ 
'''
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result


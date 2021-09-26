'''
    메소드 오버라이딩
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


class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
'''
    FourCal 클래스에 있는 div 메소드를 동일한 이름으로 다시 만드는 것 = Method Overriding
'''

a = SafeFourCal(4, 0)
print(a.div())
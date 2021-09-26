class FourCal:
    def setdata(self, first, second): # method 의 매개변수
        self.first = first # method 의 수행문 - 객체에 객체변수를 생성시킨다
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

a = FourCal()
b = FourCal()

a.setdata(4, 2)
b.setdata(3, 8)

print(a.add())
print(a.mul())
print(a.sub())
print(a.div())


class FourCal:
    def setdata(self, first, second): # method 의 매개변수
        self.first = first # method 의 수행문 - 객체에 객체변수를 생성시킨다
        self.second = second

a = FourCal()
b = FourCal()
a.setdata(4, 2)
b.setdata(3, 7)

# a 객체와 b 객체의 first(객체변수) 주소 값 확인
print(id(a.first))
print(id(b.first))

'''
    객체변수는 그 객체의 고유 값을 저장할 수 있는 공간!
    객체변수는 다른 객체들 영향을 받지 않고 독립적으로 그 값을 유지한다
'''
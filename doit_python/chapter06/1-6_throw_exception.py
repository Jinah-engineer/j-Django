'''
    오류 일부러 발생시키기
'''
class Bird:
    def fly(self):
        raise NotImplementedError   # Bird 클래스를 상속받는 자식 클래스는 반드시 fly 함수를 구현해야 한다

class Eagle(Bird):
    # def fly(self):
    #     print('very fast!')
    pass

eagle = Eagle()
eagle.fly()
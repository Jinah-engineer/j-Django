class Unit:

    # __init__ : 생성자 --> 초기화
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print('{0} 유닛이 생성되었습니다.'.format(self.name))
        print('체력 {0}, 공격력 {1}'.format(self.hp, self.damage))

marine1 = Unit('marine', 40, 5)
marine2 = Unit('marine', 40, 5)

tank = Unit('tank', 150, 35)

# parameter 개수를 맞춰줘야 한다
# marine3 = Unit('marine')
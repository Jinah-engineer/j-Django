# 일반 유닛

class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):

        # ***** inheritance
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        # self = 자기 자신 (이 클래스 자기 자신에 있는 멤버 변수의 값을 출력)
        print('{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}' \
            # location 은 전달받은 값을 출력
              .format(self.name, location, self.damage))

    def damaged(self, damage):
        print('{0} : {1} 데미지를 입었습니다.'.format(self.name, damage))
        self.hp -= damage
        print('{0} : 현재 체력은 {1} 입니다.'.format(self.name, self.hp))

        if self.hp <= 0:
            print('{0} : 파괴되었습니다.'.format(self.name))

# medic : 의무병


# 파이어뱃 : 공격 유닛, 화염 방사기.
firebat1 = AttackUnit('firebat', 50, 16)
firebat1.attack('5시')

# Assume that firebat has attacked twice
firebat1.damaged(25)
firebat1.damaged(25)



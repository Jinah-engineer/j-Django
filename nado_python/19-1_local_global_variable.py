# global
gun = 10

def checkpoint(soldiers): # 경계 근무
    # local
    gun = 20
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint2(soldiers): # 경계 근무
    # global : 전역 공간에 있는 gun 사용
    global gun
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2)  # 2명이 경계 근무 나감
print("남은 총 : {0}".format(gun))

print('-----------------------------------------------')

# return 된 gun value 는 global space 에서 사용 가능하다
def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun , 2)
print("남은 총 : {0}".format(gun))
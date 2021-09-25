import time
start_war = input('핵전쟁을 시작하시겠습니까?')
count = list(range(1, 11))
count.reverse()

if start_war == '시작':
    for i in count:
        print(i)
        time.sleep(1)
        print('발사')
        time.sleep(1)
else:
    pass

print('전쟁 종료')
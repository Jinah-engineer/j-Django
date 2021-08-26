# print('대기번호 : 1')
# print('대기번호 : 2')
# print('대기번호 : 3')
# print('대기번호 : 4')

# 하지만 100 명이라면?

for waiting_no in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_no))

print('------------------------------------')

for waiting_no in range(5): #0, 1, 2, 3, 4
    print("대기번호 : {0}".format(waiting_no))

print('------------------------------------')

for waiting_no in range(1, 6):  # 0, 1, 2, 3, 4
    print("대기번호 : {0}".format(waiting_no))

print('------------------------------------')

starbucks = ['아이언맨', '토르', '그루트']
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))
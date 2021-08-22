from random import *
lst = [1, 2, 3, 4, 5]
print(lst)

# shuffle : 무작위로 값을 섞어준다
shuffle(lst)
print(lst)

print(sample(lst, 1))

# 댓글 이벤트 - 작성자 중 1명은 치킨, 3명은 커피 쿠폰
# 추첨 프로그램 작성하기

# 조건 1 : 편의상 댓글은 20명이 작성하였고, 아이디는 1~20이라고 가정
# 조건 2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# 조건 3 : random 모듈의 shuffle 과 sample 을 활용

# idLst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
users = range(1, 21) # 1부터 21직전까지
print(type(users)) # range != list

users = list(users)
print(users)

shuffle(users)
print(users)

winners = sample(users, 4) # 4명 중 1명은 치킨, 3명은 쿠폰

print('당첨자 발표 !!!')
print('치킨 당첨자 : {0}'.format(winners[0]))
print('치킨 당첨자 : {0}'.format(winners[1:]))
print('축하합니다 !!!')







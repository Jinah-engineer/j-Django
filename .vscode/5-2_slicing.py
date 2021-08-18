idNumber = '990120-1234567'

print('성별 : ' + idNumber[7])

# 0~2 직전까지 (= 0~1)
print("연도 : " + idNumber[0:2])

print('월 : ' + idNumber[2:4])

print('일 : ' + idNumber[4:6])

# 처음부터 ~ 6직전까지
print("생년월일 : " + idNumber[:6])

# 7번째부터 ~ 끝까지
print("뒤 7 자리 : " + idNumber[7:])

# 뒤에서 7번째부터 ~ 끝까지
print('뒤 7자리 (뒤에부터) : ' + idNumber[-7:])


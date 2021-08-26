# 표준 체중을 구하는 프로그램을 작성하시오.
# 표준 체중 = 각 개인의 키에 적당한 체중

# 성별에 따른 공식
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 조건 1 : 표준 체중은 별도의 함수 내에서 계산
# ** 함수명 : std_weight
# ** 전달값 : 키(weight), 성별(gender)

# 조건 2 : 표준 체중은 소수점 둘째자리까지 표시

# Example
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

print('키를 적으세요.')
height = input()
print('성별을 적으세요.')
gender = input()

def std_weight(height, gender):
    print('키 : ' + height)
    print('성별 : ' + gender)
    if gender == '남자' or '남성' or '남':
        stdweight = int(height) * int(height) * 22 / 10000
        print('키 {0}cm {1}의 표준 체중은 {2}입니다.'.format(height, gender, stdweight))
    elif gender == '여자' or '여성' or '여':
        stdweight = int(height) * int(height) * 21 / 10000
        print('키 {0}cm {1}의 표준 체중은 {2}입니다.'.format(height, gender, round(stdweight)))

std_weight(height, gender)


print('-----------------------------------------')

def std_weight2(height, gender): # 키 m 단위 (실수), gender (성별) = 남자, 여자
    if gender == '남자':
        return height * height * 22
    else:
        return height * height * 21

height = 175  # cm 단위
gender = '남자'
weight = round(std_weight2(height / 100, gender))
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

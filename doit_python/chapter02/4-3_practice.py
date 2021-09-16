# 홍길동 씨의 평균 점수
import numpy as np
score = np.array([80, 75, 55])
print(score.mean())

# 자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법
if 13 % 2 == 0:
    print(True)
else:
    print(False)

# 홍길동 씨의 주민등록번호는 881120-1068234이다.
# 홍길동 씨의 주민등록번호를 연월일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해보자.
pin = '881120-1068234'
yyyymmdd = pin[:6]
print(yyyymmdd)
num = pin[:-8]
print(num)

# 주민등록번호 뒷자리의 맨 첫 번째 수는 성별을 나타낸다.
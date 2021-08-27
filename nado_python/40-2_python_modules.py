# glob : 경로 내의 ㅍ로더 / 파일 목록 조회 (Window -> dir)
import glob
print(glob.glob(('*.py')))

# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd())  # 현재 dir 표시

# folder = 'sample_dir'
#
# if os.path.exists(folder):
#     print('이미 존재하는 폴더입니다.')
#     os.rmdir(folder) # 폴더 삭제
#     print(folder, '폴더를 삭제!')
# else:
#     os.makedirs(folder) # 폴더 생성
#     print(folder, '폴더를 생성!')

print(os.listdir())

# time : 시간 관련 함수
import time
print(time.localtime())
# time format
print(time.strftime('%Y-%m-%d %H:%M:%S'))

import datetime
print('오늘 날짜는 ', datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일 저장
print('우리가 만난지 100일은', today + td) # 오늘부터 100일 후

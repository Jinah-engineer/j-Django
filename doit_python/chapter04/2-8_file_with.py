'''
    with 문과 함께 사용하기
        : 파일을 열고 닫는 것을 자동으로 처리
'''

with open('새파일2.txt', 'w') as f:
    f.write('life is too short, you need python.')
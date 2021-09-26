'''
    오류 회피하기
'''
try:
    f = open('새파일2.txt', 'r')
except FileNotFoundError:
    pass
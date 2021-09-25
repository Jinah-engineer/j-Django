import sys

args = sys.argv[1:] # argv : 명령창에서 입력한 인수
for i in args:
    print(i.upper(), end=' ')

'''
    argv[0] : sys1.py
    argv[1] : aaa
    argv[2] : bbb
    argv[3] : ccc
'''
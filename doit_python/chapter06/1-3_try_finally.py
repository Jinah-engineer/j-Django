'''
    try ... finally
'''
'''
    보통 finally 절은 사용한 리소스를 close 해야 할 때 많이 사용한다
'''
f = open('새파일.txt', 'w', encoding='utf-8')
try:
    f.write('hello, i\'m jinah')
finally:
    f.close()

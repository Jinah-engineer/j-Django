'''
    예외 만들기
'''

class MyError(Exception):
    def __str__(self): # 오류 메시지를 print 문으로 출력할 경우에 호출되는 메소드
        return '허용되지 않습니다.'

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

try:
    say_nick('천사')
    say_nick('바보')
except MyError as e:
    print('허용되지 않는 별명입니다.')
    print(e)

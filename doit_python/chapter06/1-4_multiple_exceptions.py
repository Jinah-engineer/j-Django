'''
    여러 개의 오류 처리하기
'''
try:
    a = [1, 2]
    print(a[3])
    4 / 0
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except IndexError as e:
    print('인덱싱할 수 없습니다.')
    print(e)


try:
    a = [1, 2]
    print(a[3])
    4 / 0
except (ZeroDivisionError, IndexError) as e:
    print(e)
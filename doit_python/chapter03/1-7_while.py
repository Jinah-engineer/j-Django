"""
    while 문 : 조건문이 참인 동안에 하위 문장들을 반복 실행한다
"""

treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print('나무를 %d번 찍었습니다.' % treeHit)
    if treeHit == 10:
        print('나무 넘어갑니다.')

print('='*20 + 'Example' + '='*20)

prompt = """
    1. Add
    2. Del
    3. List
    4. Quit
    Enter number:
"""

number = 0
while number != 4:
    print(prompt)
    number = int(input())




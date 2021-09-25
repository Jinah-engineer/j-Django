'''
    프로그램의 외부에 저장된 파일을 읽는 여러 가지 방법
'''
'''
    2. readlines 함수 사용하기
    
        : 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 돌려준다. 
'''
f = open('새파일.txt', 'r', encoding='utf-8')
lines = f.readlines()
for line in lines:
    print(line)
f.close()
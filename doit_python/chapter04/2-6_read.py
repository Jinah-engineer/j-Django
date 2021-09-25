'''
    프로그램의 외부에 저장된 파일을 읽는 여러 가지 방법
'''
'''
    3. read 함수 사용하기
    
        : 파일의 내용 전체를 문자열로 돌려준다
'''
f = open('새파일.txt', 'r', encoding='utf-8')
data = f.read()
print(data)
f.close()
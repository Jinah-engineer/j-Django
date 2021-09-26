print('='*20, 'sys', '='*20)
'''
    1. sys : 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
    
    - 명령 행에서 인수 전달하기 = sys.argv
    - 강제로 스크립트 종료하기 = sys.exit
    - 자신이 만든 모듈 불러와 사용하기 = sys.path.append 
'''
import sys
print(sys.argv)


print('='*20, 'pickle', '='*20)
'''
    2. pickle : 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈
'''
import pickle
f = open("test2.txt", 'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)
f.close()

f = open('test2.txt', 'rb')
data = pickle.load(f)
print(data)


print('='*20, 'os', '='*20)
'''
    3. os : 환경 변수나 디렉터리, 파일 등의 os 자원을 제어할 수 있게 해주는 모듈
    
    - 내 시스템의 환경 변수 값을 알고 싶을 때 = os.environ
    - 현재 디렉터리 위치 변경하기 = os.chdir
    - 현재 자신의 디렉터리 위치 돌려받기 = os.getcwd 
    - 현재 디렉터리에서 시스템 명령어 호출하기  = os.system
    - 시스템 명령어를 실행한 결과값을 읽기 모드 형태의 파일 객체로 돌려받기 = os.popen
    
    - 디렉터리 생성 = os.mkdir(디렉터리)
    - 디렉터리 삭제 = os.rmdir(디렉터리)  --- 단, 디렉터리가 비어있어야 삭제 가능
    - 파일 지우기 = os.unlink(파일 이름)
    - src 라는 이름의 파일을 dst 라는 이름으로 바꾸기 = os.rename(src,dst)
'''
import os
print(os.environ)
print(os.environ['PATH'])
print(os.system("dir"))

f = os.popen("dir")
print(f.read())


from doit_python.game.sound.echo import echo_test
def render_test():
    print('render')
    echo_test()

print(render_test())

'''
    relative package 
        
        - relative 접근자는 모듈 안에서만 사용해야 한다
'''
from ..sound.echo import echo_test
def render_test():
    print('render')
    echo_test()

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")  # end >> print 문이 끝날 때 줄바꿈을 하지 않고 계속 출력한다는 의미
#     print(lang1, lang2, lang3, lang4, lang5)
#

# 가변 인자 *args : 서로 다른 개수의 값을 넣어줄 때 활용 가능하다
def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")  # end >> print 문이 끝날 때 줄바꿈을 하지 않고 계속 출력한다는 의미
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "python", "java", "c", "c++", "c#")
profile("김태호", 25, "kotlin", "swift", "", "", "")


def profile(name, age, main_lang):
    print(name, age, main_lang)

# 아래와 같이 parameter 의 순서가 뒤바껴 있어도 결과는 잘 출력된다.

profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호")


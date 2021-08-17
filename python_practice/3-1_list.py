# list 변수 선언
students = ["egoing", "sori", "maru"]
grades = [2, 1, 4]

print(students[1]) #sori
print("len(students)", len(students))

print(min(grades))
print(max(grades))
print(sum(grades))

# statistics
import statistics
print(statistics.mean(grades)) # average

import random
print(random.choice(students)) # random하게 값을 뽑아준다
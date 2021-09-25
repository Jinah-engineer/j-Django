# continue
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60: continue
    print("%d번 학생 축하합니다. 합격입니다." % number)

print('='*30 + 'for and range 함수' + '='*30)

# range
a = range(10)
print(a) # range(0, 10) = 0 부터 10 미만의 숫자를 포함하는 range 객체

b = range(1, 11)
print(b)


print('='*30 + 'Example 01' + '='*30)
# Example 01
add = 0
for i in range(1, 11):
    add = add + i

print(add)


print('='*30 + 'Example 02' + '='*30)
# Example 02
for number in range(len(marks)):
    if marks[number] < 60: continue
    print("%d번 학생 축하합니다. 합격입니다." % (number + 1))

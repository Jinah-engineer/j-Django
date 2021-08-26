from numpy import number

print(2 + 3 * 4) #14
print((2 + 3) * 4) #20
print('----------------------')

number = 2 + 3 * 4 #14
print(number)
print('----------------------')
number = number + 2 #16
print(number)
print('----------------------')

number += 2 #18
print(number)
print('----------------------')

number *= 2 #36
print(number)
print('----------------------')

number /= 2 #18
print(number)
print('----------------------')

number -= 2 #16
print(number)
print('----------------------')

number %= 2 #0
print(number)
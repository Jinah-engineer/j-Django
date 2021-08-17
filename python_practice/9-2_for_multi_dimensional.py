persons = [
    ['egoing', 'Seoul', 'Web'],
    ['basta', 'Seoul', 'IOT'],
    ['blackdew', 'Tongyeong', 'ML']
]
print(persons[0][0])
print('---------------------------------')

for person in persons:
    print(person[0] + ', ' + person[1] + ', ' + person[2])
print('---------------------------------')

person = ['egoing', 'Seoul', 'Web']
name = person[0]
address = person[1]
interest = person[2]
print(name, address, interest)
print('---------------------------------')

name, address, interest = ['egoing', 'seoul', 'web']
print(name, address, interest)
print('---------------------------------')
for name, address, interest in persons:
    print(name + ', ' + address + ', ' + interest)
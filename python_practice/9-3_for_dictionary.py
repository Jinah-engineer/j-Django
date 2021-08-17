person = {'name' : 'egoing', 'address' : 'seoul', 'interest' : 'web'}
print(person['name'])

for key in person:
    print(key, person[key])

print('-------------persons-----------------')

persons = [
{'name' : 'egoing', 'address' : 'seoul', 'interest' : 'web'},
{'name' : 'basta', 'address' : 'seoul', 'interest' : 'iot'},
{'name' : 'blackdew', 'address' : 'cc', 'interest' : 'ml'}
]

for person in persons:
    for key in person:
        print(key, ':', person[key])
    print('-----------------------------')
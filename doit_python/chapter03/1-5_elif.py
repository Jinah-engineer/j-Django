# elif
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print('take a taxi!')
elif card:
    print('take a taxi.')
else:
    print('just walk, please!')

# if 문을 한 줄로 작성하기
if 'money' in pocket: pass
else: print('take out card.')


siteAddress = 'http://naver.com'
dot = siteAddress.index('.')
pw_front_pre = siteAddress[7:dot]
pw_front = pw_front_pre[:3]
pw_len = len(pw_front_pre)
eCount = pw_front_pre.count('e')
print(pw_front + str(pw_len) + str(eCount) + '!')

print('-----------------------------------------')

url = "http://naver.com"
my_str = url.replace("http://", "")
print(my_str)

my_str = my_str[:my_str.index('.')]
print(my_str)

password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + '!'
print("{0}의 비밀번호는 {1} 입니다." .format(url, password))
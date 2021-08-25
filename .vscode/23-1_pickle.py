import pickle
# wb = write binary (pickle 에서는 binary 만 사용)
profile_file = open("profile.pickle", "wb")
profile = {'이름':'박명수', '나이' : 30, '취미':['축구','골프', '코딩']}
print(profile)
# profile 에 있는 정보를 file 에 저장
pickle.dump(profile, profile_file)
profile_file.close()

print('-------------------------------------------')

# rb = read binary
profile_file = open("profile.pickle", 'rb')
# file 에 있는 정보를 profile 에 불러오기
profile = pickle.load(profile_file)
print(profile)
profile_file.close()
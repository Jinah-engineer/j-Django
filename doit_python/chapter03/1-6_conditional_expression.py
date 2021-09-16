score = int(input('점수 입력 >> '))

if score >= 60:
    message = "success"
else:
    message = "failure"

# ==

message = "success" if score >= 60 else "failure"

print(message)
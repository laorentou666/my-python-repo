score = int(input("Enter your score: "))
if score >= 90:
    print("You are a Good!")
elif score >= 80 and score < 90:
    print("良好")
elif score >= 70 and score < 80:
    print("及格")
else:
    print("不及格")
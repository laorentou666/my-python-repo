name = input("Enter your name: ")
age = int(input("Enter your age: "))
score = [float(x) for x in input("Enter your score: ").split()] # 列表推导式
sum = sum(score)
avg = sum/len(score)
print(f"你好,{name},今年{age}岁,总分{sum},平均分{avg:.2f}")
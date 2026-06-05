data_dict = {}
with open("student.txt", "r",encoding="utf-8") as f: #在with内传encoding参数
    for line in f.readlines():
        line = line.strip().split(",")
        key,value = line[0],line[1] # 要先分别对应上，line[0]是名字/学号，line[1]是分数
        data_dict[key] = int(value) #建议在这里就转一道到int，省的下文再每次都转
    print(data_dict)

    sum_grade = 0
    passed_count = 0
    for value in data_dict.values(): #.values提取字典中所有的值，.keys所有的键，.items所有的键值对
        sum_grade += int(value)
    for temp in data_dict.values():
        if temp >= 60:
            passed_count += 1
    print(f"avg_grade = {sum_grade/len(data_dict.values())}")
    print(f"max_grade = {max(data_dict.items(),key  = lambda x: x[1])}")
    # max_student, max_grade = max(data_dict.items(), key=lambda x: x[1]) 通过逗号拆成两个变量
    print(f"passed_num = {passed_count}")
    with open("student.txt","a",encoding="utf-8")as f:
        f.write("\n")
        f.write(f"avg_grade = {sum_grade/len(data_dict.values())}\n")
        f.write(f"max_grade = {max(data_dict.items(),key = lambda x: x[1])}\n")
        f.write(f"passed_num = {passed_count}\n")

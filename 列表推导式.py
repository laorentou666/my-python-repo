students = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 78},
    {"name": "赵六", "score": 92},
    {"name": "孙七", "score": 66},
]
print("大于等于80学生")
for student in students:
    if student["score"] >= 80:
        print(student["name"])
print("\n")
for name in students:
    print(name["name"])

print("\n")

sort_score = sorted(students, key=lambda student: student["score"],reverse=True)
for student in sort_score:
    print(student["name"],student["score"])

print("\n")

for student in students:
    if student["score"] >= 60:
        student["passed"] = True
print(students)

#列表推导式不会啊w，先写着for循环吧，这次没卡很久，有点进步好吧
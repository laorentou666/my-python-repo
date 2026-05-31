stu = {
    "姓名": input("输入姓名"), # py字典可以直接在元素内input
    "年龄": int(input("输入年龄")),
    "身高": round(float(input("输入身高")),2), # 再套一层round
    "是否成年": ""
}

if stu["年龄"] >= 18:
    stu["是否成年"] = "True"
else:
    stu["是否成年"] = "False"

for x,y in stu.items ():
    print(x,y)
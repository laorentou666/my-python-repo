a = input("输入a边长度: ")
b = input("输入b边长度: ")
c = input("输入c边长度: ")
if a + b > c and b + c >a and c + a >b: # 三个条件都要满足,不能用or,反例3,4,10
    print("可以构成三角形")
else:
    print("不可以构成三角形")
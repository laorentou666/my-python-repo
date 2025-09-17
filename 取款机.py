balance = 1000
while True:
    qukuanjine = int(input("输入取款金额: "))
    if qukuanjine > balance:
        print("取款金额大于余额，请重新输入") #因为没有break所以死循环
    else:
        print(f"取款成功 剩余余额{balance - qukuanjine}")
        break #break了退出程序
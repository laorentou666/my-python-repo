num1 = input("输入被除数")
num2 = input("输入除数")

try:
    print(int(num1) / int(num2))
except ValueError:
    print("number must be int")
except ZeroDivisionError:
    print("除数不能为0")
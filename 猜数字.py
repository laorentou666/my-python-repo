import random
number =random.randint(1,100)
count  = 0

while True:
    inputs = (input("input number")) # 先不着急转成int
    if inputs == "q":
        break
    elif inputs.isalpha():
        print("illegal input")
        break
    if int(inputs) > number:
        print("too big")
        count += 1
    elif int(inputs) < number:
        print("too small")
        count += 1
    else:
        print(f"right, number is {number}")
        break

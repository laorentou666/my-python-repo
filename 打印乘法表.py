for i in range(1,10): #包前不包后
    for j in range(1,i + 1):
        print(f"{i} x {j} ={i * j}", end="\t") #转义字符空四格
    print() #换行

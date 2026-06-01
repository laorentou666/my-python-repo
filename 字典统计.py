text = "banana"
count  = {}
for char in text:
    if char in count:
        count[char] += 1 #count[char],char就是字典里面的键，比如b,a
    else:
        count[char] = 1
print(count)

counted = sorted(count.items(), key=lambda x: x[1], reverse=True) # lambda的x[1]是元组索引，x[0]即字符。x[1]即次数
# count.items()。它把字典的结构解开，打包成了一个列表，列表里面的每一个元素都是一个元组
for word, count in counted:
    print(f"{word}: {count}")
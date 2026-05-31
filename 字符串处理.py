str = "hello python world python"
print(len(str))
print(f"单词数量{len(str.split())}") # len和str这个字符串类还有什么方法？这么方便，我还打算写个for呢
for word in str.split():
    if word == "python":
        print("有python")
        break
print(str.replace("python", "java")) # 我最开始写的是先replace，再print(str)，为什么没有效果？如果是c语言，给变量赋新值了不应该变吗（在 Python 中，字符串是不可变对象（Immutable）任何对字符串的操作（如 replace()、upper()、strip()）都不会修改原字符串，而是生成并返回一个全新的字符串。）
list = str.split()
print(list)
print(list[::-1])
reversed_words = " ".join(str.split()[::-1]) # 先分割，split返回一个列表，再切片，再用join以空格拼成一个新的字符串，所以reversed word是列表还是字符串？字符串
print(f"反转后的句子（单词反转）：{reversed_words}")
print(str[::-1]) # 如果是str[:0:-1]，不包后，句首的h不会被输出

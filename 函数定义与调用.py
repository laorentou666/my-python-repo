def get_lower(str): # 定义
    last = str[-1]
    if last.isupper():
        last = last.lower()
    print(last)
str = "C-LanguagE"
get_lower(str) # 调用
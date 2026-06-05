classa = set(["张三", "李四", "王五", "赵六"])
classb = set(["王五", "赵六", "孙七", "周八"])
print(f"两个班所有的:{list(classa | classb)}") # |并集
print(f"两个班都在的{set.intersection(classb, classa)}") # 交集，并集union
print(f"只在a班的{classa - classb}") #差集
print(f"只在b班的{classb - classa}")
print(f"只在一个班出现的{set.symmetric_difference(classb, classa)}") # 对称差集
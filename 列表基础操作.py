from numpy.ma.extras import average

nums = [3,5,1,9,2,8,5]
nums.append(10)
print(f"添加后的列表{nums}")
nums.remove(5)
print(nums)
print(max(nums)) #为什么不是num.max?
print(min(nums))
print(sum(nums))
print(average(nums))
print(sorted(nums))
print(sorted(nums, reverse=True)) # 降序
for num in nums:
    if num % 2 == 0:
        print(f"偶数{num}")
# for num1 in nums:
#     if num1 > average(nums):
#         print(num1)

print([num1 for num1 in nums if num1 > average(nums)]) # 列表推导式，还有字典推导式
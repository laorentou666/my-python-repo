import  math

def add(a,b):
    return a+b
def is_prime(a):
    if a < 2:
        return False
    else:
        return all(a % x != 0 for x in range(2, int(math.sqrt(a))+1)) # 类似于列表推导式，注意左闭右开，可以用all返回所有符合条件的值


def get_max(number):
    return max(number)

if __name__ == '__main__':
    number = [1,2,3,4,5]
    print(add(1,2))
    print(is_prime(2))
    print(get_max(number))
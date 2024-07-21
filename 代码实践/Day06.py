# def foo():
#     print("hello,world!")

# def foo():
#     print("goodbye,world!")
# # python没有重载
# # foo()

# if __name__ == "__main__":
#     foo()
# #s实现最大公因数和最小公倍数
# def gcd(x,y):
#     (x,y) = (x,y) if x > y else (y,x)
#     while y != 0:
#         x,y = y,x%y
#     # for i in range (y, 0, -1):
#     #     if x % i == 0 and y % i == 0:
#     #         return i
#     return x
# print(gcd(48,24))

# def lcm(x,y):
#     return x*y//gcd(x,y)
# print(lcm(2,4))

#判断回文数
def fun(num):
    # if str(num) == str(num)[::-1]:
    #     print("true")
    # else:
    #     print("false")
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp = temp // 10
    if total == num:
        print("true")
    else:
        print("false")
fun(123)
fun(121)
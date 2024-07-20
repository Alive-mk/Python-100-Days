# def foo():
#     print("hello,world!")

# def foo():
#     print("goodbye,world!")
# # python没有重载
# # foo()

# if __name__ == "__main__":
#     foo()

def gcd(x,y):
    (x,y) = (x,y) if x > y else (y,x)
    while y != 0:
        x,y = y,x%y
    # for i in range (y, 0, -1):
    #     if x % i == 0 and y % i == 0:
    #         return i
    return x
print(gcd(48,24))

def lcm(x,y):
    return x*y//gcd(x,y)
print(lcm(2,4))
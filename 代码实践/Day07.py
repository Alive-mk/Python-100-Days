# s1 = '\'hello, world!\''
# s2 = '\n\\hello, world!\\\n'
# print(s1, s2, end='')

# s1 = '\141\142\143\x61\x62\x63'
# s2 = '\u9a86\u660a'
# print(s1, s2)

# s1 = r'\'hello, world!\''
# s2 = r'\n\\hello, world!\\\n'
# print(s1, s2, end='')

# a, b = 5, 10
# print('%d * %d = %d' % (a, b, a * b))
# print("{} * {} = {}".format(a, b, a * b))
# print(f"{a} * {b} = {a*b}")

# list1 = [1, 3, 5, 7, 100]
# # 添加元素
# list1.append(200)
# print(list1)
# list1.insert(1, 400)
# print(list1)

# list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
# list2 = sorted(list1)
# print(list2)
# import sys
# list1 = [x+y for x in "ABCDE" for y in "12345"]
# print(list1)
# print(sys.getsizeof(list1))

# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#         yield a


# def main():
#     for val in fib(20):
#         print(val)


# if __name__ == '__main__':
#     main()

# # 定义元组
# t = ('骆昊', 38, True, '四川成都')
# print(t)

set1 = {1, 2, 3, 3, 3, 2}
set1.add(4)
set1.update([11, 12])
print(set1)

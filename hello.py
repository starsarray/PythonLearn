"""
文件注释
"""
# 单行注释
'''
1多行注释
2多行注释
'''
# 输出语句
print("Hello, World!")
# 算术运算符
a = 2
b = 3
c = 0
print("a + b =", a + b)
c = a - b
print("a - b =", c)
c = a / b
print("a / b =", c)
c = a // b
print("a // b =", c)
c = a * b
print("a * b =", c)
c = a ** b
print("a ** b =", c)
c = a % b
print("a % b =", c)
# 赋值运算符
a = 2
a += 3
print("a += 3 =", a)
a = 2
a -= 3
print("a -= 3 =", a)
a = 2
a *= 3
print("a *= 3 =", a)
a = 2
a /= 3
print("a /= 3 =", a)
a = 2
a //= 3
print("a //= 3 =", a)
a = 2
a **= 3
print("a **= 3 =", a)
a = 2
a %= 3
print("a %= 3 =", a)
# 比较运算符
a = 2
b = 3
print("a == b =", a == b)
print("a!= b =", a!= b)
print("a < b =", a < b)
print("a <= b =", a <= b)
print("a > b =", a > b)
print("a >= b =", a >= b)
# 逻辑运算符
a = True
b = False
print("a and b =", a and b)
print("a or b =", a or b)
print("not a =", not a)
# 条件语句
a = 2
b = 3
if a > b:
    print("a > b")
elif a < b:
    print("a < b")
else:
    print("a == b")
# 循环语句
for i in range(5):
    print(i)
for i in range(2, 5):
    print(i)
for i in range(2, 10, 3):
    print(i)
while a < 5:
    print(a)
    a += 1
# 函数
def my_func(a, b):
    return a + b
print("my_func(a, b) =", my_func(2, 3))
# 类
class MyClass:
    def __init__(self, x):
        self.x = x
    def my_method(self):
        return self.x * 2
my_obj = MyClass(3)
print("my_obj.x =", my_obj.x)
print("my_obj.my_method() =", my_obj.my_method())
# 异常处理
try:
    a = 1 / 0
except ZeroDivisionError:
    print("Error: division by zero")
finally:
    print("Cleaning up...")
# 输入输出语句
# name = input("Enter your name: ")
# print("Hello, " + name + "!")
print('\'Hello, world!\'')  # 输出：'Hello, world!'
print("Hello, world!\nHow are you?")  # 输出：Hello, world!
                                      #      How are you?
print("Hello, world!\tHow are you?")  # 输出：Hello, world!    How are you?
print("Hello,\b world!")  # 输出：Hello world! (退格)
# print("Hello,\f world!")  # 输出：Hello world! (换页符)
print("Hello,\r world!")  # 输出：Hello world! (回车符)
# print("Hello,\v world!")  # 输出：Hello world! (垂直制表符)
# print("Hello,\a world!")  # 输出：Hello world! (响铃)
print("Hello,\033[31mworld!\033[0m")  # 输出：Hello \033[31mworld!\033[0m (红色字体)
print("Hello,\033[42mworld!\033[0m")  # 输出：Hello \033[42mworld!\033[0m (背景色为绿色)
print("Hello,\033[1mworld!\033[0m")  # 输出：Hello \033[1mworld!\033[0m (粗体)
print("Hello,\033[4mworld!\033[0m")  # 输出：Hello \033[4mworld!\033[0m (下划线)
print("Hello,\033[33;44mworld!\033[0m")  # 输出：Hello \033[33;44mworld!\033[0m (黄色字体背景色为蓝色)
print("A 对应的 ASCII 值为：", ord('A'))  # 输出：A 对应的 ASCII 值为： 65
print("65 对应的字符为：", chr(65))  # 输出：65 对应的字符为： A
print("Hello, world!".encode('utf-8'))  # 输出：b'Hello, world!' (UTF-8 编码)
print(b'Hello, world!'.decode('utf-8'))  # 输出：Hello, world! (UTF-8 解码)
# print("Hello, world!".encode('gbk'))  # 输出：b'\xb2\xd4\xca\xc7\xd2\xbb\xca\xc0' (GBK 编码)
# print(b'\xb2\xd4\xca\xc7\xd2\xbb\xca\xc0'.decode('gbk'))  # 输出：Hello, world! (GBK 解码)
print("Hello, world!".encode('ascii'))  # 输出：b'Hello, world!' (ASCII 编码)
print(b'Hello, world!'.decode('ascii'))  # 输出：Hello, world! (ASCII 解码)



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
# # 输入输出语句
# # name = input("Enter your name: ")
# # print("Hello, " + name + "!")
# print('\'Hello, world!\'')  # 输出：'Hello, world!'
# print("Hello, world!\nHow are you?")  # 输出：Hello, world!
#                                       #      How are you?
# print("Hello, world!\tHow are you?")  # 输出：Hello, world!    How are you?
# print("Hello,\b world!")  # 输出：Hello world! (退格)
# # print("Hello,\f world!")  # 输出：Hello world! (换页符)
# print("Hello,\r world!")  # 输出：Hello world! (回车符)
# # print("Hello,\v world!")  # 输出：Hello world! (垂直制表符)
# # print("Hello,\a world!")  # 输出：Hello world! (响铃)
# print("Hello,\033[31mworld!\033[0m")  # 输出：Hello \033[31mworld!\033[0m (红色字体)
# print("Hello,\033[42mworld!\033[0m")  # 输出：Hello \033[42mworld!\033[0m (背景色为绿色)
# print("Hello,\033[1mworld!\033[0m")  # 输出：Hello \033[1mworld!\033[0m (粗体)
# print("Hello,\033[4mworld!\033[0m")  # 输出：Hello \033[4mworld!\033[0m (下划线)
# print("Hello,\033[33;44mworld!\033[0m")  # 输出：Hello \033[33;44mworld!\033[0m (黄色字体背景色为蓝色)
# print("A 对应的 ASCII 值为：", ord('A'))  # 输出：A 对应的 ASCII 值为： 65
# print("65 对应的字符为：", chr(65))  # 输出：65 对应的字符为： A
# print("Hello, world!".encode('utf-8'))  # 输出：b'Hello, world!' (UTF-8 编码)
# print(b'Hello, world!'.decode('utf-8'))  # 输出：Hello, world! (UTF-8 解码)
# # print("Hello, world!".encode('gbk'))  # 输出：b'\xb2\xd4\xca\xc7\xd2\xbb\xca\xc0' (GBK 编码)
# # print(b'\xb2\xd4\xca\xc7\xd2\xbb\xca\xc0'.decode('gbk'))  # 输出：Hello, world! (GBK 解码)
# print("Hello, world!".encode('ascii'))  # 输出：b'Hello, world!' (ASCII 编码)
# print(b'Hello, world!'.decode('ascii'))  # 输出：Hello, world! (ASCII 解码)

# 进制转换
decimal_number = 42
binary_number = bin(decimal_number)  # 十进制转换为二进制
print('转换为二进制:', binary_number)  # 转换为二进制: 0b101010

octal_number = oct(decimal_number)  # 十进制转换为八进制
print('转换为八进制:', octal_number)  # 转换为八进制: 0o52

hexadecimal_number = hex(decimal_number)  # 十进制转换为十六进制
print('转换为十六进制:', hexadecimal_number) # 转换为十六进制: 0x2a

# 字符串运算符
string1 = "Hello, "
string2 = "world!"
string3 = string1 + string2
print(string3)  # 输出：Hello, world!

string4 = "Hello, " * 3
print(string4)  # 输出：Hello, Hello, Hello,

string5 = "Hello, " + "world!"
print(string5[0:5])  # 输出：Hello
print(string5[6:11]) # 输出： worl

string6 = " Hello, world!"
print(string6)  # 输出：Hello, world!
print(string6.upper())  # 输出：HELLO, WORLD!
print(string6.lower())  # 输出：hello, world!
print(string6.replace("l", "x"))  # 输出：Hxxo, worxd!
print(string6.split(","))  # 输出：['Hello','world!']
print(string6.strip())  # 输出：Hello, world!
print(string6.startswith("H"))  # 输出：False
print(string6.endswith("d!"))  # 输出：True
print(string6.find("l"))  # 输出：3
print(string6.count("l"))  # 输出：3
print(string6.isalpha())  # 输出：False
print(string6.isdigit())  # 输出：False
print(string6.isalnum())  # 输出：False
print(string6.isspace())  # 输出：False
print(string6.islower())  # 输出：False
print(string6.isupper())  # 输出：False
print(string6.istitle())  # 输出：False
print(string6.isnumeric())  # 输出：False
print(string6.isdecimal())  # 输出：False
print(string6.isidentifier())  # 输出：False
print(string6.isprintable())  # 输出：True
print(string6.isascii())  # 输出：True

if "Hello" in string6:
    print("Substring 'Hello' found in the string")  # 输出：Substring 'Hello' found in the string
else:
    print("Substring 'Hello' not found in the string")  # 输出：Substring 'Hello' not found in the string
print (r'\n') # 原始字符串 不进行转义
print (R'\n 2' + "\n 2")

# 字符串格式化
print ("我叫 %s 今年 %d 岁!" % ('小明', 10))
print ("{0} 说：{1} 好！".format('小明', '你好'))
print ("{name} 说：{word} 好！".format(name='小明', word='你好'))

para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
a = ('s'
     '2')
print(para_str)
print(a)

name = 'Alice'
print(f'Hello {name}')  # 替换变量
print(f'Hello {name.upper()}')  # 调用方法 全部大写
print(f'Hello {name.lower()}')  # 调用方法 全部小写
print(f'Hello {name.title()}')  # 调用方法 首字母大写
print(f'Hello {name.swapcase()}')  # 调用方法 大小写反转
print(f'Hello {name[0]}')  # 索引
print(f'Hello {name[1:3]}')  # 切片
print(f'Hello {name[1:]}')  # 切片
print(f'Hello {name[:3]}')  # 切片
print(f'Hello {name.replace("i", "I")}')  # 调用方法
print(f'Hello {name.split("e")}')  # 调用方法

# 列表 [] 可修改
my_list = [1, 2, 3, 4, 5]
print(my_list)
print(my_list[0])
print(my_list[1:3])
print(my_list[1:])
print(my_list[:3])
print(my_list[1:3])
print(my_list + [6, 7, 8])
print(my_list * 2)
print(3 in my_list)
print(3 not in my_list)
print(my_list[::-1] # 反转列表
      )
my_list.append(6) # 追加元素
print(my_list)
my_list.insert(1, 4) # 插入元素
print(my_list)
my_list.remove(4) # 删除第一个值为 4 的元素
print(my_list)
my_list.pop(1) # 删除指定位置元素
print(my_list)
my_list.sort() # 排序
print(my_list)
my_list.reverse() # 反转
print(my_list)
my_list.clear() # 清空列表
print(my_list)

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
xx = a + n
print(x)
print(xx)

# 元组 () 不可修改
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(my_tuple[0])
print(my_tuple[1:3])
print(my_tuple[1:])
print(my_tuple[:3])
print(my_tuple[1:3])
print(my_tuple + (6, 7, 8))
print(my_tuple * 2)
print(3 in my_tuple)
print(3 not in my_tuple)
# 字典 {} 键值对
my_dict = {'name': 'Alice', 'age': 20, 'city': 'Beijing'}
print(my_dict)
print(my_dict['name'])
print(my_dict['age'])
print(my_dict['city'])
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print('name' in my_dict)
print('Alice' in my_dict.values())
print(my_dict.get('name'))
print(my_dict.get('gender', 'unknown'))
my_dict['age'] = 21
print(my_dict)
my_dict.update({'gender': 'female'})
print(my_dict)
my_dict.pop('age')
print(my_dict)
my_dict.clear()
print(my_dict)




# PythonLearn
Python学习之旅
***
## 目录
***
## 基础语法
### 编码
默认情况下，Python 3 源码文件以 UTF-8 编码，所有字符串都是 unicode 字符串
### 标识符
在 Python 3 中，可以用中文作为变量名，非 ASCII 标识符也是允许的了
### 注释
多行注释可以用多个 # 号，还有 ''' 和 """
### 多行语句
Python 允许使用反斜杠（\）将一行代码分为多行
Python 可以在同一行中使用多条语句，语句之间使用分号 ; 分割
### print输出

```py
print( "Hello", end="" ) # 不换行输出
```

### import 与 from...import
在 python 用 import 或者 from...import 来导入相应的模块。

- 将整个模块(somemodule)导入，格式为： import somemodule

- 从某个模块中导入某个函数,格式为： from somemodule import somefunction

- 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc

- 将某个模块中的全部函数导入，格式为： from somemodule import *
---
## 数据类型
在Python中变量没有类型，它是动态语言，不需要声明变量的类型。
类型是变量所指的内存中对象的类型。
### 标准数据类型
不可变数据类型：**重新赋值，则id() 变化**

1. Number（数字）:**int、float、bool、complex（复数）**

2. String（字符串）

3. Tuple（元组）

可变数据类型：**改变值，id() 不变**

4. List（列表）

5. Set（集合）

6. Dictionary（字典）

**此外还有一些高级的数据类型，如: 字节数组类型(bytes)。**

### Number（数字）
Python3 支持 int、float、bool、complex（复数）
**注意：Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加， True==1、False==0 会返回 True，但可以通过 is 来判断类型。**

*在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。*

```py
math.ceil(4.1) # 返回 5
math.floor(4.9) # 返回 4
math.fabs(-10) # 返回10.0 以浮点数形式返回数字的绝对值
math.log(100,10) #返回2.0

random.choice(range(10)) # 从0到9中随机挑选一个整数
```



### bytes 类型
bytes 类型是 Python3 中新增的数据类型，它是不可变序列，用于存储二进制数据。
bytes 类型中的元素是整数值（0 到 255 之间的整数），而不是 Unicode 字符。
创建 bytes 类型的方法有两种：

1. 使用 bytes() 函数，它第一个参数是要转换的对象，第二个参数是编码方式，如果省略第二个参数，则默认使用 UTF-8 编码
```python
x = bytes("hello", encoding="utf-8")
```
2. 使用 b'' 前缀，它将字符串中的每个字符转换为对应的 ASCII 字符
```python
x = b"hello"
```
---
## 运算符



### 优先级

| 运算符                                                       | 描述                               |
| ------------------------------------------------------------ | ---------------------------------- |
| `(expressions...)`,`[expressions...]`, `{key: value...}`, `{expressions...}` | 圆括号的表达式                     |
| `x[index]`, `x[index:index]`, `x(arguments...)`, `x.attribute` | 读取，切片，调用，属性引用         |
| await x                                                      | await 表达式                       |
| `**`                                                         | 乘方(指数)                         |
| `+x`, `-x`, `~x`                                             | 正，负，按位非 NOT                 |
| `*`, `@`, `/`, `//`, `%`                                     | 乘，矩阵乘，除，整除，取余         |
| `+`, `-`                                                     | 加和减                             |
| `<<`, `>>`                                                   | 移位                               |
| `&`                                                          | 按位与 AND                         |
| `^`                                                          | 按位异或 XOR                       |
| `|`                                                          | 按位或 OR                          |
| `in,not in, is,is not, <, <=, >, >=, !=, ==`                 | 比较运算，包括成员检测和标识号检测 |
| `not x`                                                      | 逻辑非 NOT                         |
| `and`                                                        | 逻辑与 AND                         |
| `or`                                                         | 逻辑或 OR                          |
| `if -- else`                                                 | 条件表达式                         |
| `lambda`                                                     | lambda 表达式                      |
| `:=`                                                         | 赋值表达式                         |



***
## 字符串

String（字符串）是Python中最常用的数据类型。字符串可以用单引号（''）或双引号（""）括起来，同时使用反斜杠（\）转义特殊字符。
### 字符串创建

```py
# 单行
s = "Hello, world!"
s = 'Hello, world!'
# 多行 并且带格式
s = '''Hello, 
world'''
s = """Hello, 
world"""
```

### 索引

![img](https://static.jyshare.com/wp-content/uploads/123456-20200923-1.svg)

### 格式化字符串

- %

```py
>>> name = 'Runoob'
>>> 'Hello %s' % name
'Hello Runoob'
```

- f-string 是 python3.6 之后版本添加的，称之为字面量格式化字符串

```py
>>> name = 'Runoob'
>>> f'Hello {name}'  # 替换变量
'Hello Runoob'
>>> f'{1+2}'         # 使用表达式
'3'

>>> w = {'name': 'Runoob', 'url': 'www.runoob.com'}
>>> f'{w["name"]}: {w["url"]}'
'Runoob: www.runoob.com'
```

在 Python 3.8 的版本中可以使用 **=** 符号来拼接运算表达式与结果：

```py
>>> x = 1
>>> print(f'{x+1}')   # Python 3.6
2

>>> x = 1
>>> print(f'{x+1=}')   # Python 3.8
x+1=2
```


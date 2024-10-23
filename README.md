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
多行注释可以用多个 `# `，还有` '''` 和`"""`
### 多行语句
Python 允许使用反斜杠`\`将一行代码分为多行
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

String（字符串）是Python中最常用的数据类型。字符串可以用单引号`''`或双引号`""`括起来，同时使用反斜杠`\`转义特殊字符。
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

- `%`

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

***

## 列表
- 用`[]`表示
- 列表**可变**
***
## 元组
- 用`()`表示
- 元组**不可变**
- 元组中只包含一个元素时，需要在元素后面**添加逗号** **,** ，否则括号会被当作运算符使用
***
## 字典
- 用`{}`表示，里面是键值对的形式
- 字典是无序的，键值对没有先后顺序
- 字典的键必须是**不可变**的，所以可以用数字，字符串或元组充当，而用列表就不行
- 字典的键可以重复，但值不可以重复
- 字典用 **key** 来访问值，用 **value** 来访问键
***
## 集合
- 用`{}`表示
- 集合是无序的，元素不能重复
- 集合**可变**

创建一个空集合必须用 `set()` 而不是 `{ }`，因为` { }` 是用来创建一个空字典

***

### 推导式

列表推导式外面是`[]`，集合推导式外面是`{}`，元组推导式外面是`()`

```py
[变量表达式 for 变量 in 序列] 
或者 
[变量表达式 for 变量 in 序列 if 条件]
```

***

###  迭代器

通过 `next()` 函数逐步获取数据，而不是一次性将所有数据加载到内存中。这对于处理大数据集非常有用

```py
>>> list=[1,2,3,4]
>>> it = iter(list)    # 创建迭代器对象
>>> print (next(it))   # 输出迭代器的下一个元素
1
>>> print (next(it))
2
>>>
```

***

### 生成器

- 生成器是特殊类型的迭代器，可以在不保存整个序列的情况下迭代数据，在需要时生成值，非常适合处理大量数据或无限序列

- 当在生成器函数中使用 **yield** 语句时，函数的执行将会暂停，并将 **yield** 后面的表达式作为当前迭代的值返回

```py
def my_generator(limit):
    current = 0
    while current < limit:
        yield current
        current += 1

# 使用生成器
for num in my_generator(5):
    print(num)
```

***

## 函数

### 关键字参数

允许函数调用时参数的顺序与声明时不一致

```py
def printme( str ):
   print (str)
   return
printme( str = "hello")
```

### 不定长参数

- 参数名前加`*`，会以元组(tuple)的形式导入，存放所有未命名的变量参数。

```py
def my_func(x,*y):
    print(x)
    print(y)
my_func(1,2,3)
```

```py
1
(2, 3)
```



- 参数名前加`**`，会以字典的形式导入，存放所有未命名的关键字参数

```py
def my_func(x,**y):
    print(x)
    print(y)
my_func(1,a=2,b=3)
```

```py
1
{'a': 2, 'b': 3}
```

- 单独出现星号 `*`，则星号` * `后的参数必须用关键字传入

```py
def my_func(x,*,a,b):
    print(x);print(a);print(b)
my_func(3,a=2,b=3)
```

```py
3
2
3
```

### 匿名函数

Python 使用 **lambda** 来创建匿名函数，**lambda**只是一个表达式

语法：

```py
lambda [arg1 [,arg2,.....argn]]:expression
```

```py
sum = lambda arg1, arg2: arg1 + arg2
print ("相加后的值为 : ", sum( 10, 20 ))
```

lambda 函数通常与内置函数如 map()、filter() 和 reduce() 一起使用，以便在集合上执行操作。例如：

## 强制位置参数

Python3.8 新增了一个函数形参语法 `/` 用来指明`/`前的函数形参必须使用指定位置参数，不能使用关键字参数的形式

在以下的例子中，形参 a 和 b 必须使用指定位置参数，c 或 d 可以是位置形参或关键字形参，而 e 和 f 要求为关键字形参:

```py
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)
```

```py
f(10, 20, 30, d=40, e=50, f=60)
```
**位置参数必须在前，关键字参数必须在后**
***

## 装饰器

装饰器是一种函数，它接受一个函数作为参数，并返回一个新的函数或修改原来的函数

装饰器的语法使用 **`@`+装饰器名** 来应用在函数或方法上

```py
# 记录函数的执行时间
import time

def timer(func): # 定义装饰器timer
    def wrapper(*args, **kwargs):
        startTime = time.time()
        res = func() # 开始执行函数func(),也就是传来的myFunction()
        endTime = time.time()
        print(f'执行时间：{endTime - startTime:.2f}秒') # 计算函数的执行时间
        return res
    return wrapper

@ timer
def myFunction():
    time.sleep(1)
    print('函数执行完毕')

myFunction()
```

```py
函数执行完毕
执行时间：1.00秒
```

装饰器常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景

***

## 数据结构

### 列表

| 方法              | 描述                                                         |
| :---------------- | :----------------------------------------------------------- |
| list.append(x)    | 把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]          |
| list.extend(L)    | 通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L  |
| list.insert(i, x) | 在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) |
| list.remove(x)    | 删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。 |
| list.pop([i])     | 从列表的指定位置移除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被移除（方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号，你会经常在 Python 库参考手册中遇到这样的标记。） |
| list.clear()      | 移除列表中的所有项，等于del a[:]                             |
| list.index(x)     | 返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误 |
| list.count(x)     | 返回 x 在列表中出现的次数                                    |
| list.sort()       | 对列表中的元素进行排序                                       |
| list.reverse()    | 倒排列表中的元素                                             |
| list.copy()       | 返回列表的浅复制，等于a[:]                                   |

- 列表当做栈（后进先出）
- 列表当做队列（先进先出），使用`pop()`这类操作的时间复杂度为O(n)，可以选择用`collections.deque，它是双端队列，可以在两端高效地添加和删除元素

~~~py
from collections import deque
# 创建一个空队列
queue = deque()
# 向队尾添加元素
queue.append('a')
queue.append('b')
print("队列状态:", queue)  # 输出: 队列状态: deque(['a', 'b'])
first_element = queue.popleft()# 从队首移除元素
print("移除的元素:", first_element)  # 输出: 移除的元素: a
print("队列状态:", queue)            # 输出: 队列状态: deque(['b'])
~~~

### 遍历技巧

在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来：

```py
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
...
gallahad the pure
robin the brave
```

在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到：

```py
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe
```

同时遍历两个或更多的序列，可以使用 zip() 组合：

```py
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
```

***

## 模块

- 目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包
- 如果包定义文件 **__init__.py** 存在一个叫做 **__all__** 的列表变量，那么在使用 **from package import \*** 的时候就把这个列表中的所有名字作为包内容导入
- 更新包之后要保证 **__all__** 也更新
- 推荐用**from Package import specific_submodule**这种方法
- 主模块的名字永远是"__main__"

***

## 输入输出

### 输出

将输出的值转成字符串

- **str()：** 函数返回一个用户易读的表达形式
- **repr()：** 产生一个解释器易读的表达形式

```py
>>> s = 'Hello, Runoob'
>>> str(s)
'Hello, Runoob'
>>> repr(s)
"'Hello, Runoob'"
>>> str(1/7)
'0.14285714285714285'
>>> x = 10 * 3.25
>>> y = 200 * 200
>>> s = 'x 的值为： ' + repr(x) + ',  y 的值为：' + repr(y) + '...'
>>> print(s)
x 的值为： 32.5,  y 的值为：40000...
>>> #  repr() 函数可以转义字符串中的特殊字符
... hello = 'hello, runoob\n'
>>> hellos = repr(hello)
>>> print(hellos)
'hello, runoob\n'
>>> # repr() 的参数可以是 Python 的任何对象
... repr((x, y, ('Google', 'Runoob')))
"(32.5, 40000, ('Google', 'Runoob'))"
```

####  `str.format() `可使输出的形式更加多样

位置及关键字参数可以任意的结合:

```py
>>> print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))
站点列表 Google, Runoob, 和 Taobao。
```

**!a** (使用 **ascii()**), **!s** (使用 **str()**) 和 **!r** (使用 **repr()**) 可以用于在格式化某个值之前对其进行转化:

```py
>>> import math
>>> print('常量 PI 的值近似为： {}。'.format(math.pi))
常量 PI 的值近似为： 3.141592653589793。
>>> print('常量 PI 的值近似为： {!r}。'.format(math.pi))
常量 PI 的值近似为： 3.141592653589793。
```

在` :` 后传入一个整数, 可以保证该域至少有这么多的宽度

在` :` 后传入`.nf`，则表示保留n位小数，f为浮点型

#### `%`（将被淘汰）

```py
>>> print('常量 PI 的值近似为：%5.3f 和 %6.4f。' % (math.pi ,math.pi))
常量 PI 的值近似为：3.142 和 3.1416。
```

### 输入

#### 读取键盘输入`input()`

```py
str = input("请输入：")
```

#### 读和写文件

只能保存字符串，其他格式需要先转化成字符串

```py
# 打开一个文件
f = open("/tmp/foo.txt", "w") #只写 文件若存在，从头编辑，反之创建文件
f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
# 关闭打开的文件
f.close()
# 打开一个文件
f = open("/tmp/foo.txt", "r") #只读
str = f.read()
print(str)
# 关闭打开的文件
f.close()
```

### pickle 模块

python的pickle模块实现了基本的数据序列和反序列化，够将程序中运行的对象信息保存到文件中去，永久存储

基本接口：

```py
pickle.dump(obj, file, [,protocol])
```

```py
import pickle,pprint
# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}
selfref_list = [1, 2, 3]
selfref_list.append(selfref_list) # 引用自身，会无限递归
output = open('data.pkl', 'wb')
# Pickle dictionary using protocol 0.
pickle.dump(data1, output)
# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)
output.close()
#使用pickle模块从文件中重构python对象
pkl_file = open('data.pkl', 'rb')
data1 = pickle.load(pkl_file)
pprint.pprint(data1)
data2 = pickle.load(pkl_file)
pprint.pprint(data2)
pkl_file.close()
```

```py
{'a': [1, 2.0, 3, (4+6j)], 'b': ('string', 'Unicode string'), 'c': None}
[1, 2, 3, <Recursion on list with id=2210685513920>]
```

***

## 错误与异常

![img](https://www.runoob.com/wp-content/uploads/2019/07/try_except_else_finally.png)

### 预定义的清理行为

一些对象定义了标准的清理行为，无论系统是否成功的使用了它，一旦不需要它了，那么这个标准的清理行为就会执行

`with`  `as`

```py
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```

以上这段代码执行完毕后，就算在处理过程中出问题了，文件 f 总是会关闭

***

## 面相对象

### 类方法

- 类有一个名为 __init__() 的特殊方法（**构造方法**），该方法在类实例化时会自动调用
- 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的**第一个参数名称**, 按照惯例它的名称是 self

### 继承

```py
#多继承
class sample(speaker,student):
```

### 方法重写

如果父类方法的功能不能满足需求，可以在子类重写父类的方法

```py
class Parent:        # 定义父类
   def myMethod(self):
      print ('调用父类方法')
 
class Child(Parent): # 定义子类
   def myMethod(self):
      print ('调用子类方法')
 
c = Child()          # 子类实例
c.myMethod()         # 子类调用重写方法
super(Child,c).myMethod() #用子类对象调用父类已被覆盖的方法
```

```py
调用子类方法
调用父类方法
```

***

## 命名空间

- **内置名称（built-in names**）， Python 语言内置的名称，比如函数名 abs、char 和异常名称 BaseException、Exception 等等
- **全局名称（global names）**，模块中定义的名称，记录了模块的变量，包括函数、类、其它导入的模块、模块级的变量和常量
- **局部名称（local names）**，函数中定义的名称，记录了函数的变量，包括函数的参数和局部定义的变量。（类中定义的也是）

![img](https://www.runoob.com/wp-content/uploads/2014/05/types_namespace-1.png)

## 作用域

- **L（Local）**：最内层，包含局部变量，比如一个函数/方法内部
- **E（Enclosing）**：包含了非局部(non-local)也非全局(non-global)的变量。比如两个嵌套函数，一个函数（或类） A 里面又包含了一个函数 B ，那么对于 B 中的名称来说 A 中的作用域就为 nonlocal
- **G（Global）**：当前脚本的最外层，比如当前模块的全局变量
- **B（Built-in）**： 包含了内建的变量/关键字等，最后被搜索

![img](https://www.runoob.com/wp-content/uploads/2014/05/1418490-20180906153626089-1835444372.png)

### global 和 nonlocal关键字

当内部作用域想修改外部作用域的变量时，就要用到 global 和 nonlocal 关键字

***

## 

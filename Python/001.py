# Python标识符
# 标识符是用来标识变量、函数、类、模块等名称的字母数字组合

# 标识符的命名规则：
# 1. 必须以字母或下划线开头
# 2. 不能以数字开头
# 3. 严格区分大小写        username ≠ UserName ≠ USERNAME
# 4. 只能使用字母、数字、下划线 a-z A-Z 0-9 _ 其他字符全部非法！    


# Python变量命名规则：（坦克撞击墙壁）
# 1. 小驼峰：tankHitWall          # 首字母小写，后续单词首字母大写
# 2. 大驼峰：TankHitWall          # 单词首字母大写
# 3. 下划线：tank_hit_wall        # 全小写，多个单词用下划线链接
# 4. 全大写：TANKHITWALL          # 常量：不会发生变化的数据(圆周率、自然常数)


'''
Python保留字
Python有35个保留字, 不能用作标识符
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 
'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 
'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 
'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))


'''
f-string 格式化字符串 format 
特点是可以直接在字符串书写{}，使其可以在字符串中嵌入变量值，{}中的字段会被替换成变量的值。

整数形的占位符为 %d
%d 表示输出整数，%06d表示输出必须为 6 位数，如果不足 6 位数则用 0 补齐

浮点数的占位符为 %f
%f 表示输出浮点数，%.1f / %.2f 表示保留 1 / 2 位小数

字符串占位符为 %s
%s 表示输出字符串，%s 后面可以跟字符串变量

百分数的占位符为 %
% 为Python中的特殊字符, 如果需要输出百分数，则需要用 %% 转义

若 % 后有多个数据则必须使用括号并用逗号隔开，如：
print("Hello, %s! Your score is %.2f" % ('Alice', 85.5678))

若 % 后只有一个数据则不需要括号，或者在括号中的数据后加上逗号，如：
print("Hello, Alice! Your score is %.2f" % 85.5678)
print("Hello, Alice! Your score is %.2f" % (85.5678, ))
'''


'''
Python数据类型
格式: 
    变量名 = 变量值

查看变量名类型: 
    type(变量名)

name = input("请输入您的姓名：")
name = 变量
= 赋值运算符 
input() 输入函数
'''

# Python有6种基本数据类型: 数字型（整数型、浮点型、布尔型）、字符串型、列表型、元组型、集合型、字典型

# 1. 数字型
# 1.1 整数型 int 整数数据
num1=3
print(f'num1={num1}, type(num1)={type(num1)}')


# 1.2 浮点型 float 小数数据
num2=3.14
print(f'num2={num2}, type(num2)={type(num2)}')


# 1.3 布尔型 bool 逻辑值 True/False（只有两个值，对应真和假）
visited=True  # visited=False 表示还没有访问过
print(f'visited={visited}, type(visited)={type(visited)}')


# 2. 字符串型 str 字符串数据 有三种书写格式 1. 单引号 2. 双引号 3. 三引号（多行数据书写）
# name1 = 'Alice'      # 单引号
# name2 = "Alice"      # 双引号
# name3 = '''Alice'''  # 三引号
# name4 = “““Alice”””  # 三引号
name='Alice'
print(f'name={name}, type(name)={type(name)}')


# 3. 列表型 list 列表数据（有序，可重复，可扩展，可修改）
fruits=['apple', 'banana', 'orange', 'apple', 'banana', 'orange']  # 列表的元素用逗号隔开, 可扩展，可修改
print(f'fruits={fruits}, type(fruits)={type(fruits)}')

fruits.append('grape')                # 向列表中添加元素
print(f'fruits={fruits}, type(fruits)={type(fruits)}')

fruits.remove('banana')               # 从列表中删除元素
print(f'fruits={fruits}, type(fruits)={type(fruits)}')


# 4. 元组型 tuple 元组数据（有序，可重复，不可扩展，不可修改）
fruits=('apple', 'banana', 'orange', 'apple', 'banana', 'orange')  # 元组的元素必须用逗号隔开，且不可修改
print(f'fruits={fruits}, type(fruits)={type(fruits)}')


# 5. 集合型 set 集合数据（无序，不可重复，可扩展, 可修改）
fruits={'apple', 'banana', 'orange', 'apple', 'banana', 'orange'}  # 集合的元素用逗号隔开, 可扩展，可修改
print(f'fruits={fruits}, type(fruits)={type(fruits)}')

fruits.add('grape')                   # 向集合中添加元素
print(f'fruits={fruits}, type(fruits)={type(fruits)}')

fruits.remove('banana')               # 从集合中删除元素
print(f'fruits={fruits}, type(fruits)={type(fruits)}')


# 6. 字典型 dict 字典数据（键值对）
person={'name': 'Alice', 'age': 25, 'city': 'Beijing'}
print(f'person={person}, type(person)={type(person)}')
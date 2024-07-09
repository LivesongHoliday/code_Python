'''
Python数据类型
格式: 
    变量名 = 变量值

查看变量名类型: 
    type(变量名)

name = input("请输入您的姓名：")
name = 变量
= 赋值运算符 (运算符前后应该有‘一个空格’)
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
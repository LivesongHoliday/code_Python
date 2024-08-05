'''
整数型, 浮点型, 字符串型之间的相互转换
格式：
    1. 整数型 int(变量) int(字符串) int(浮点型)
    2. 浮点型 float(变量) float(字符串) float(整数型)
    3. 字符串型 str(变量) str(整数型) str(浮点型)
'''
# 字符串型 (两个字符串相加, 其结果就是字符串相拼接)
# 字符串 + 字符串 = 字符串
# 网页中的输入框 : input() 函数可以接收用户输入的字符串 ( 网页中的输入框获取的数据都是字符串类型的 )
num1 = '10'
num2 = '20'
result = num1 + num2
print(f'result = {result}')

# 字符串型转整数型
# 整数型 + 整数型 = 整数型
num1 = '10'
num2 = '20'
result = int(num1) + int(num2)
print(f'result = {result}')

# 字符串型转浮点型
# 浮点型 + 浮点型 = 浮点型
num1 = '10.5'
num2 = '20.3'
result = float(num1) + float(num2)
print(f'result = {result}')

# 整数型转字符串型
# 字符串型 + 字符串型 = 字符串型
num1 = 10
num2 = 20
result = str(num1) + str(num2)
print(f'result = {result}')

# 浮点型转字符串型
# 字符串型 + 字符串型 = 字符串型
num1 = 10.5
num2 = 20.3
result = str(num1) + str(num2)
print(f'result = {result}')

# 浮点型转整数型 (直接舍弃小数部分, 不会进行四舍五入)
# 整数型 + 整数型 = 整数型 (精度丢失)
num1 = 10.5
num2 = 20.3
result = int(num1) + int(num2)
print(f'result = {result}')                  # 10 + 20 = 30

# 整数型转浮点型 
# 浮点型 + 浮点型 = 浮点型 (精度提高)
num1 = 10
num2 = 20
result = float(num1) + float(num2)
print(f'result = {result}')

# 整数型 + 浮点型 = 浮点型
num1 = 10
num2 = 20.3
result = float(num1) + num2
print(f'result = {result}')
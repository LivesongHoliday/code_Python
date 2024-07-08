"""
 转义字符（ 反斜杠 ):
 \ + 字符 改变原有字符的含义
 
 \t 制表符     (类似于四个空格)
 \n 换行符     (换行)
 \r 回车符     (回到行首)
 \b 退格符     (删除前一个字符)
 \f 换页符     (换页)
 \\ 反斜杠本身 (输出反斜杠)
 \' 单引号     (输出单引号)
 \" 双引号     (输出双引号)
"""

# end="" 用于指定输出结尾符，默认是换行符，可以指定为空字符串""，这样输出不会换行
print("Hello, World!", end="")
print("Hello, Python!")

# end="\n" 指定输出结尾符为换行符
print("Hello, World!", end="\n")
print("Hello, Python!")

# end="\t" 指定输出结尾符为制表符
print("Hello, World!", end="\t")
print("Hello, Python!")

# end="\b" 指定输出结尾符为退格符
print("Hello, World!", end="\b")
print("Hello, Python!")

# end=" " 指定输出结尾符为空格
print("Hello, World!", end=" ")
print("Hello, Python!")


# print() 输出函数 默认会自动换行
num1 = 10
num2 = 20
# 1. print 函数可以跟多个变量或字符串参数
print("num1 =", num1, "num2 =", num2)

# 2. print(f'')
print(f"num1 = {num1} num2 = {num2}")

# 3. .format() 方法可以格式化字符串
# 格式化字符串的语法是 { }，其中 {0} 表示第一个参数，{1} 表示第二个参数，计算机只能识别 0 和 1
print("num1 = {0} num2 = {1}".format(num1, num2))


'''
整数型, 浮点型, 字符串型之间的相互转化
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


'''
input() 输入函数
格式：
    input("提示信息")
    input() 函数可以接收用户输入的字符串 ( 网页中的输入框获取的数据都是字符串类型的 )
说明：
    由于 input() 函数输入会返回结果, 所以程序中必须定义一个变量接受 input() 函数的返回值。
    input() 是阻塞函数, 函数会等待用户, 输入如果用户没有输入，程序就不会继续执行。
'''
name = input('亲，请输入你的名字：')
age = input('亲，请输入你的年龄：')
print(f'大家好，我是{name}！我今年{age}岁了！')

# input() 函数返回的是 str 类型
num1 = input('请输入第一个数字：')
num2 = input('请输入第二个数字：')
sum = num1 + num2
print(f'sum = {sum}')    # sum = 1020

# 方式一: 相加前转换
num1 = input('请输入第一个数字：')
num2 = input('请输入第二个数字：')
sum = int(num1) + int(num2)
print(f'sum = {sum}')    # sum = 30

# 方式二: 直接转换
num1 = int(input('请输入第一个数字：'))
num2 = int(input('请输入第二个数字：'))
sum = num1 + num2
print(f'sum = {sum}')    # sum = 30
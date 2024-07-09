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
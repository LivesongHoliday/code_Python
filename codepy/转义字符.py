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
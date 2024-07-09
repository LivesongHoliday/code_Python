'''
算数运算符：
+ 加法
- 减法
* 乘法
/ 除法
% 取模 ( 取余 )
// 整除
** 乘方 ( 幂运算 )
'''

result1 = 10 / 3
print(f'result = {result1}')    # 3.3333333333333

result2 = 10 // 3
print(f'result = {result2}')    # 3

result3 = 10 % 3
print(f'result = {result3}')    # 1

result4 = 2 ** 3
print(f'result = {result4}')    # 2 * 2 * 2 = 8


'''
复合赋值运算符: 如果一个变量在自身的基础上发生变化, 则可以选择使用复合赋值运算符。
+= 加等于
-= 减等于
*= 乘等于
/= 除等于 
%= 取模等于
//= 整除等于
**= 乘方等于
'''

# num1 = 1
# num1 = num1 + 1
# print(f'num1 = {num1}')    # 2

num1 = 1
num1 += 1
print(f'num1 = {num1}')      # 2

# num2 = 10
# num2 = num2 - 5
# print(f'num2 = {num2}')    # 5

num2 = 10
num2 -= 5
print(f'num2 = {num2}')      # 5


# 逗号运算符: 多个表达式用逗号分隔, 并返回最后一个表达式的值。
# 原理: 元组解包

# num1 = 10
# num2 = 20
# num3 = 30
# num1, num2, num3 = 10, 20, 30

# num1, num2, num3 = 10, 20, 30, 40, 50
# ValueError: too many values to unpack (expected 3) 

num1, num2, num3 = 10, 20, 30
print(f'num1 = {num1}, num2 = {num2}, num3 = {num3}')    # num1 = 10, num2 = 20, num3 = 30

'''
比较运算符: 对变量或表达式的结果进行大小比较, 其结果是一个布尔值, 即True或False。
<  小于
<= 小于等于
>  大于
>= 大于等于
== 等于
!= 不等于
'''

num1 = 10
num2 = 20
result1 = num1 == num2
print(f'result1 = {result1}')    # False

result2 = num1 != num2
print(f'result2 = {result2}')    # True
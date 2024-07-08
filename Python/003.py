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

# 
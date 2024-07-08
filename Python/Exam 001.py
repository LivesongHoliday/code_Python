""" 
1. 定义一个字符串变量name,输出 我的名字叫小明，请多多关照！
2. 定义一个字符串变量name和一个整数变量age,输出 我的名字叫小明,今年18岁,请多多关照！
3. 定义整数变量student_no, 输出 我的学号是 000001
4. 定义一个小数price、weight、money, 输出 苹果单价 9.00 元/斤, 重量 5.00 斤, 需支付 45.00 元
5. 定义一个小数scale, 输出 数据比例是 10.00%
"""


name = ('小明')
print (f'我的名字叫{name}, 请多多关照！')


# 字符串占位符为 %s
# %s 表示输出字符串，%s 后面可以跟字符串变量
name = ('小明')
age = 18
print ('我的名字叫%s, 今年%d岁, 请多多关照！' % (name, age))

name = ('小明')
age = 18
print (f'我的名字叫{name}, 今年{age}岁，请多多关照！')


# 整数形的占位符为 %d
# %d 表示输出整数，%06d表示输出必须为 6 位数，如果不足 6 位数则用 0 补齐
student_no = 1
print ('我的学号是 %06d' % student_no)


# 浮点数的占位符为 %f
# %f 表示输出浮点数，%.1f / %.2f 表示保留 1 / 2 位小数
price = 9
weight = 5
money = price * weight
print ('苹果单价 %.2f 元/斤, 重量 %.2f 斤, 需支付 %.2f 元' % (price, weight, money))


scale = 10
print ('数据比例是 %.2f%%' % scale)

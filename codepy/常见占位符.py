'''
f-string 格式化字符串 format 
特点是可以直接在字符串书写{}，使其可以在字符串中嵌入变量值，{}中的字段会被替换成变量的值。

整数形的占位符为 %d
%d 表示输出整数, %06d表示输出必须为 6 位数，如果不足 6 位数则用 0 补齐

浮点数的占位符为 %f
%f 表示输出小数, %.1f / %.2f 表示保留 1 / 2 位小数

字符串占位符为 %s
%s 表示输出字符串, %s 后面可以跟字符串变量

百分数的占位符为 %
% 为Python中的特殊字符, 如果需要输出百分数, 则需要用 %% 转义

若 % 后有多个数据则必须使用括号并用逗号隔开, 如：
print("Hello, %s! Your score is %.2f" % ('Alice', 85.5678))

若 % 后只有一个数据则不需要括号，或者在括号中的数据后加上逗号，如：
print("Hello, Alice! Your score is %.2f" % 85.5678)
print("Hello, Alice! Your score is %.2f" % (85.5678, ))
'''
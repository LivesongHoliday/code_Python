'''
Python保留字
Python有35个保留字, 不能用作标识符
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 
'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 
'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 
'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''

import keyword                # 导入keyword模块
print(keyword.kwlist)         # 输出Python保留字列表
print(len(keyword.kwlist))    # 输出Python保留字数量
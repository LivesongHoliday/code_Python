'''
input 练习
某超市 Tshirt 单价为 56.9 元, 裤子单价 89.88 元。
顾客买了三件 Tshirt 和五件裤子, 请编写程序计算顾客购买 Tshirt 和裤子的总价。
如果今天全场 88 折, 则需要支付多少元? 
'''

tshirt_price = float(input('您买的这件Tshirt多少钱? '))
trousers_price = float(input('您买的这条裤子多少钱? '))

tshirt_num = int(input('请问您买了几件Tshirt? '))
trousers_num = int(input('请问您买了几条裤子? '))

normal_total_price = tshirt_price * tshirt_num + trousers_price * trousers_num
discount_total_price = normal_total_price * 0.88

print(f'您的购买总价为: {normal_total_price} 元, 88 折后为: {discount_total_price} 元.')
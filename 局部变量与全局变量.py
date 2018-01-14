def discounts(price,rate):
    final_price = price * rate #此处final_price为局部变量
    return final_price

old_price = float(input('请输入原价:'))
rate = float(input('请输入折扣:'))
final_price = discounts(old_price,rate)#此处final_price为全局变量,两者互不干扰
print('打完折后的价格是:',final_price)

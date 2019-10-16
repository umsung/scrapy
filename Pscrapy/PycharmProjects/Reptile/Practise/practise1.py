'''
购物车
'''

def practise():
    salary = input("请输入工资：")
    salary = int(salary)

    things = [["1、iphone","5000"],
          ["2、macpro","12000"],
          ["3、coffee","31"],
          ["4、book","81"],
          ["5、bike","800"]]
    item = []
    while True:
        num = input('请输入商品编号：').strip()
      
        if not num.isdigit() or (int(num) > 6 or int(num) < 0):
            print("请输入1-5之间的数字")
            continue

        price = things[int(num)-1][1]
        goods_name = things[int(num)-1][0]
        if num == '5':
            break
            
        if int(salary) >= int(price):
            salary = salary - int(price)
            print('成功加入购物车，当前余额为: %d' %salary)
            item.append(goods_name)
        else:
            print('余额不足')
    
    print('已加入的商品：%s, \n当前余额为：%d' %(item, salary))


if __name__ == "__main__":
    practise()

# s.isalnum() 所有字符都是数字或者字母，为真返回 Ture，否则返回 False。
# s.isalpha() 所有字符都是字母，为真返回 Ture，否则返回 False。
# s.isdigit() 所有字符都是数字，为真返回 Ture，否则返回 False。
# s.islower() 所有字符都是小写，为真返回 Ture，否则返回 False。
# s.isupper() 所有字符都是大写，为真返回 Ture，否则返回 False。
# s.istitle() 所有单词都是首字母大写，为真返回 Ture，否则返回 False。
# s.isspace() 所有字符都是空白字符，为真返回 Ture，否则返回 False。
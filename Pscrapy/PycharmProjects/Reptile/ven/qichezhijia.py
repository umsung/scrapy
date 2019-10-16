from fontTools.ttLib import TTFont


def comp(l1, l2):  # 定义一个比较函数，比较两个列表的坐标信息是否相同
    if len(l1) != len(l2):
        return False
    else:
        mark = 1
        for i in range(len(l1)):
            if abs(l1[i][0] - l2[i][0]) < 40 and abs(l1[i][1] - l2[i][1]) < 40:
                pass
            else:
                mark = 0
                break
        return mark


# 手动确定一组编码和字符的对应关系
u_list = ['uniED79', 'uniECC6', 'uniED18', 'uniEC64', 'uniECB6', 'uniEDF7', 'uniED43', 'uniED95', 'uniECE2', 'uniEC2E',
          'uniEC80', 'uniEDC1', 'uniEC1F', 'uniED5F', 'uniECAC', 'uniECFE', 'uniEC4A', 'uniED8B', 'uniEDDD', 'uniED29',
          'uniED7B', 'uniECC8', 'uniEE08', 'uniEC66', 'uniEDA7', 'uniECF3', 'uniED45', 'uniEC92', 'uniECE4', 'uniEC30',
          'uniED71', 'uniEDC3', 'uniED0F', 'uniEC5C', 'uniECAE', 'uniEDEE', 'uniEC4C', 'uniED8D']
word_list = ['的', '是', '上', '近', '小', '高', '不', '着', '八', '十', '右', '短', '三', '少', '二', '七', '九', '更', '呢', '得', '低',
             '一', '很', '大', '多', '左', '好', '长', '了', '坏', '五', '地', '和', '远', '下', '四', '六', '矮']




font1 = TTFont('qichezhijia.ttf')
font1.saveXML('qichezhijia.xml')

be_p1 = []  # 保存38个字符的（x,y）信息
for uni in u_list:
    p1 = []  # 保存一个字符的(x,y)信息
    p = font1['glyf'][uni].coordinates  # 获取对象的x,y信息，返回的是一个GlyphCoordinates对象，可以当作列表操作，每个元素是（x,y）元组
    # p=font1['glyf'][i].flags #获取0、1值，实际用不到
    for f in p:  # 把GlyphCoordinates对象改成一个列表
        p1.append(f)
    be_p1.append(p1)

font2 = TTFont('002.ttf')
uni_list2 = font2.getGlyphOrder()[1:]
on_p1 = []
for i in uni_list2:
    pp1 = []
    p = font2['glyf'][i].coordinates
    for f in p:
        pp1.append(f)
    on_p1.append(pp1)

n2 = 0
x_list = []
for d in on_p1:
    n2 += 1
    n1 = 0
    for a in be_p1:
        n1 += 1
        if comp(a, d):
            print(uni_list2[n2 - 1], word_list[n1 - 1])
            x_list.append(word_list[n1 - 1])
# 分行打印出来，方便和FontCreator中进行比较确认
print(x_list[:16])
print(x_list[16:32])
print(x_list[-6:])

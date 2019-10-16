import re
import requests
from fontTools.ttLib import TTFont
from lxml import etree


# with open('3O1RpL.woff', wb) as f:
#     f.write()

# baseFonts = TTFont('basefont.woff')
baseFonts = TTFont('E:/Pscrapy/PycharmProjects/Reptile/ven/font.woff')
baseFonts.saveXML('E:/Pscrapy/PycharmProjects/Reptile/ven/font.xml')


obj_list1=baseFonts.getGlyphNames()[1:]   # 看xml文件的<hmtx>。获取所有字符的对象，去除第一个和最后一个
print('obj_list1:', obj_list1)
# ['uniE0D3', 'uniE11F', 'uniE7A7', 'uniEB96', 'uniED89', 'uniEF34', 'uniEFB3', 'uniF430', 'uniF75F', 'uniF8AE']

uni_list1=baseFonts.getGlyphOrder()[1:]    # 看xml文件的<GlyphOrder>。获取所有编码，去除前2个
print('uni_list1:',uni_list1)
# uni_list1: ['uniE7A7', 'uniEB96', 'uniED89', 'uniEF34', 'uniF75F', 'uniF430', 'uniE0D3', 'uniF8AE', 'uniE11F', 'uniEFB3']


# print(baseFonts['glyf']['uniE7A7'])
# <fontTools.ttLib.tables._g_l_y_f.Glyph object at 0x04412630>  这个字符对象是不变的


print(baseFonts.getBestCmap())
# {120: 'x', 57555: 'uniE0D3', 57631: 'uniE11F', 59303: 'uniE7A7', 60310: 'uniEB96', 60809: 'uniED89', 61236: 'uniEF34', 61363: 'uniEFB3', 62512: 'uniF430', 63327: 'uniF75F', 63662: 'uniF8AE'}

bestcmap = baseFonts['cmap'].getBestCmap()
print(bestcmap)

print(baseFonts['glyf']['uniE2CE'].coordinates )
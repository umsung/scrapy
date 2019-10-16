# -*- coding: utf-8 -*-
"""
Spyder Editor
利用条件运算符的嵌套来完成此题：
学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
This is a temporary script file.
"""
test=input("输入成绩：")
letter=0
space=0
digit=0
others=0
for i in test:
    if i.isalpha():
        letter+=1
    elif i.isspace():
        space+=1
    elif i.isdigit():
        digit+=1
    else:
        others+=1
print('char=%d,space=%d,digit=%d,others=%d'%(letter,space,digit,others))

        

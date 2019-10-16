import os
import pathlib
from pathlib import Path

# pathlib 不单纯是对 os  中一些模块或方法进行封装，
# 而是为了兼容不同的操作系统，
# 它为每类操作系统定义了接口。
# 你希望在UNIX机器上操作Windows的路径，然
# 而直接操作是做不到的，所以为你创建了一套接口 PurePath，
# 你可以通过接口来实现你的目的（反之亦然）

print(os.path.abspath('.'))

path = (os.path.abspath(__file__)).replace('\\','/')
print((os.path.abspath(__file__)).replace('\\','/'))

print(os.path.join(path,'sad'))
# 当前路径
print((os.getcwd()).replace('\\','/'))
print(pathlib.Path.cwd())

# 去父路径
print(os.path.dirname(os.path.abspath('.')))
print(pathlib.Path.cwd().parent)

# 路径拼接
print(os.path.join(os.getcwd(),'11','22','33'))
print(pathlib.Path.cwd().joinpath('11','22','33'))
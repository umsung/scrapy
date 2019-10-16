from io import StringIO, BytesIO

f = open('file.txt', 'w', encoding='utf-8')
f.write('hello world')
f.close()

f = open('./file/file.txt', 'r')
f.read()
f.close()


# StringIO写入
f = StringIO()
f.write('')
f.close()

# StringIO读取
f = StringIO('/file/file.txt')
while True:
    s = f.readline()
    if s == '':
        break
    print(s)


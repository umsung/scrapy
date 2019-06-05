import socket
import threading
import time


def tcplink(sock, addr):
    print('Accept a new tcp connection from %s:%s...' % addr)
    print('Accept a new tcp connection from {0[0]}:{0[1]}...'.format(addr))
    sock.send('已连接welcome!'.encode())
    while True:
        data = sock.recv(1024)
        print('Receive %s' % data.decode('utf-8'))
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('hello, %s' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed' % addr)


# 服务器地址（主机，端口）
address = ('127.0.0.1', 9999)
# 初始化socket
s = socket.socket()
# 绑定地址
s.bind(address)
# 开始监听
s.listen(5)
print('【服务器已启动，主机：%s，端口：%s】' % address)
print('【等待连接中...】')
while True:
    # 接收客户端socket和地址
    sock, addr = s.accept()
    # 启动子线程处理连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

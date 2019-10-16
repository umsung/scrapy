import socket
import threading
import time
from multiprocessing import Pool, Process


# 服务器地址（主机，端口）
address = ('127.0.0.1', 9999)
# 初始化socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# 绑定地址
s.bind(address)
# 开始监听
s.listen(5)
print('【服务器已启动，主机：%s，端口：%s】' % address)
print('【等待连接中...】')
# address = ('127.0.0.1', 9999)
# s=socket(AF_INET,SOCK_STREAM)
# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# s.bind(('127.0.0.1',9999))
# s.listen(5)
# print('【服务器已启动，主机：%s，端口：%s】' % address)
# print('【等待连接中...】')

def tcplink(sock, addr):
    print('Accept a new tcp connection from %s:%s...' % addr)
    print('Accept a new tcp connection from {0[0]}:{0[1]}...'.format(addr))
    sock.send('已连接welcome!'.encode())
    while True:
        r_data = sock.recv(1024)
        print('Receive: %s' % r_data.decode('utf-8'))
        time.sleep(1)
        if not r_data or r_data.decode('utf-8') == 'exit':
            break

        # s_data = input('请输入发送的内容：').strip()
        s# sock.send('test'.encode('utf-8'))
        # sock.send(s_data.encode('utf-8'))

    sock.close()
    print('Connection from %s:%s closed' % addr)


if __name__ == "__main__":
 

    p = Pool(3) # 进程池中进程数量默认是cpu核数
    while True:
        # 接收客户端socket和地址
        sock, addr = s.accept()
        # 启动子线程处理连接
        # t = threading.Thread(target=tcplink, args=(sock, addr))
        # t.start()

        # 使用进程池 
        p.apply_async(tcplink, args=(sock,addr))


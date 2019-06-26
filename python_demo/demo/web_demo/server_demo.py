import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 监听端口：
s.bind(('127.0.0.1', 9999))

# 等待连接的最大量
s.listen(5)
print("Waiting for connection")


def tcplink(socket, addr):
    print('Accept new connection from %s:%s...' % (socket, addr))

    socket.send(b'Welcome!')
    while True:
        data = socket.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        socket.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))

    socket.close()
    print('Connection from %s:%s closed.' % addr)


while True:
    # 接收新的连接
    socket, addr = s.accept()

    t = threading.Thread(target=tcplink, args=(socket, addr))
    t.start()

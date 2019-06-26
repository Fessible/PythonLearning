import socket

# ipv4 使用面向流的协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接
s.connect(("www.sina.com.cn", 80))

# print(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# 发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

buffer = []
while True:

    # 每次最多接收1k字节
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

print(buffer)
data = b''.join(buffer)
print(data)

# 关闭连接
s.close()

header, html = data.split(b'\r\n\r\n', 1)

print("header: ", header)
print("html: ", html)

print(header.decode('utf-8'))

# 把数据写入文件
with open('sina.html', 'wb') as f:
    f.write(html)

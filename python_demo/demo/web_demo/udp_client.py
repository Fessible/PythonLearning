import socket

# # socket.SOCK_DGRAM
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
# # 发送数据
# for data in [b'Michael', b'Tracy', b'Sarah']:
#     # 发送数据
#     s.sendto(data, ('127.0.0.1', 9999))
#
#     print(s.recv(1024).decode('utf-8'))
#
# s.close()

hostname = 'www.python.org'
addr = socket.gethostbyname(hostname)
print("The Ip address of {} is {}".format(hostname, addr))

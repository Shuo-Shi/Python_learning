import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # SOCK_STREAM指定使用面向流的TCP协议; SOCK_DGRAM则指定了这个Socket的类型是UDP

# 监听端口:
s.bind(('127.0.0.1', 9999))
# 调用listen()方法开始监听端口
s.listen(5)
print('Waiting for connection...')

# 连接建立后，服务器首先发一条欢迎消息，然后等待客户端数据，并加上Hello再发送给客户端。如果客户端发送了exit字符串，就直接关闭连接。
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()


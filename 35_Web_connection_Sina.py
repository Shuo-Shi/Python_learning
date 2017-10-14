# 导入socket库:
import socket

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 创建Socket时，AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6。
# SOCK_STREAM指定使用面向流的TCP协议，这样，一个Socket对象就创建成功，但是还没有建立连接。

# 建立连接:
s.connect(('www.sina.com.cn', 80))
# 注意参数是一个tuple，包含地址和端口号。
# 80端口是Web服务的标准端口。其他服务都有对应的标准端口号，例如SMTP服务是25端口，FTP服务是21端口，等等。
# 端口号小于1024的是Internet标准服务的端口，端口号大于1024的，可以任意使用。

# 发送请求数据，要求返回首页内容:
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# 发送的文本格式必须符合HTTP标准
# 每个Header一行一个，换行符是\r\n。当遇到连续两个\r\n时，Header部分结束，后面的数据全部是Body。

# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

# 关闭连接:
s.close()

# 接收到的数据包括HTTP头和网页本身，我们只需要把HTTP头和网页分离一下，把HTTP头打印出来，网页内容保存到文件
header, html = data.split(b'\r\n\r\n',1) # 参数1表示分割次数为1次
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)
# 只需要在浏览器中打开这个sina.html文件，就可以看到新浪的首页了。

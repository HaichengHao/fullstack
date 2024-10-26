# @Author    : 百年
# @FileName  :server.py.py
# @DateTime  :2024/10/26 15:44
import socket
server = socket.socket()
server.bind(('127.0.0.1',8080))
server.listen(5)

while True:
    conn,addr = server.accept()
    data = conn.recv(1024)
    print(f'data:{data}')
    # 路径解析
    request_path = data.decode('utf-8').split('\r\n')[0].split('')[1]

    if request_path == '/':
        with open('index.html','rb') as f:
            data = f.read()
        conn.send(b'HTTP/1.1 200 OK\r\n\r\n'+data)
    elif request_path == 'timer':
        with open('login.html','rb') as f:
            data = f.read()
        conn.send(b'HTTP/1.1 200 OK\r\n\r\n'+data)
    else:
        with open('notFound.html','rb') as f:
            data = f.read()
        conn.send(b'HTTP/1.1 200 OK\r\n\r\n'+data)

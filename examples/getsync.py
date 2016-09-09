# coding: utf-8

import time
import socket

start = time.time()


def get(path):
    s = socket.socket()
    # s.connect(('localhost', 8090))
    s.connect('https://grade.muxixyz.com/api/')

    request = 'GET %s HTTP/1.0\r\n\r\n' % path
    s.send(request.encode())

    buf = []
    chuck = s.recv(1000)
    if chuck:
        buf.append(chuck)
    else:
        body = b''.join(buf).decode()
        return body.split('\n')[0]


# get 发起请求(客户端)
get('/hello/')
get('/hello/')

print('%0.2f' % (time.time() - start))

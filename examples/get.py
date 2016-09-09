# coding: utf-8

import threading
import socket
import time

start = time.time()


def get(path):

    s = socket.socket()
    s.connect(('localhost', 8090))
    request = 'GET %s HTTP/1.0\r\n\r\n' % path
    s.send(request.encode())

    buf = []
    while True:
        chuck = s.recv(1000)
        if chuck:
            buf.append(chuck)
        else:
            body = b''.join(buf).decode()
            print body.split('\n')[0]
            return


def main():
    thread_pool = [
        threading.Thread(target=get, name='get1', args=('/hello/',)),
        threading.Thread(target=get, name='get2', args=('/hello/',)),
    ]

    for thread in thread_pool:
        thread.start()

    for thread in thread_pool:
        thread.join()

# get('/hello/')
# get('/hello/')
main()
print "%.2f" % (time.time() - start)

#!/usr/bin/env python3

import threading
import time




class Connections():
    def __init__(self):
        self.connections = []
        self.timer = 0

    def __iter__(self):
        return self.connections

    def __add__(self, new_connection):
        # assert type(other, Connection), "Can only add Connection to connections"
        self.connections.append(new_connection)
        new_connection.start_timeout_counter()
        print('Added new connection!')
        new_connection.run()

    def kill(self, connection):
        self.connections.remove(connection)


class Connection(threading.Thread):
    tid = 0

    def __init__(self, conn, addr, container, timeout=10, name="null"):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        self.name = name
        self.timeout = 10
        self.inactive = 0
        self.container = container
        Connection.tid += 1
        self.lock = threading.Lock()

    def run(self):
        """Server code!"""
        with self.conn:
            print('Connected by', self.addr)
            while True:
                data = self.conn.recv(1024)
                with self.lock:
                    if data.decode() == 'close':
                        self.join()
                        break
                    self.conn.sendall(data)
                    self.inactive = 0

    def timeout(connection):
        while True:
            time.sleep(1)
            with connection.lock:
                connection.inactive += 1
                if connection.inactive > connection.timeout:
                    print('timeout reached')
                    break
        connection.join()

    def join(self):
        with self.lock:
            self.conn.send(b'CLOSE')
            self.conn.close()
            print('closed connection')
            self.container.kill(self)
            Connection.tid -= 1

    def start_timeout_counter(self):
        threading.Thread(target=self.timeout, args=(self, )).start()


import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

connections = Connections()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        connections.__add__(Connection(conn, addr, container=connections))

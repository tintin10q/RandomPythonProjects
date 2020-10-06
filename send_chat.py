import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def send(s, message):
    s.send(message.encode())
    data = s.recv(1024)
    return data
import threading
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


    def join(self):
        with self.lock:
            self.conn.send(b'CLOSE')
            self.conn.close()
            print('closed connection')
            self.container.kill(self)
            Connection.tid -= 1

    def start_timeout_counter(self):
        threading.Thread(target=timeout,
                         args=(self,), ).start()


# ok done

while True:
    message = input("M:")
    response = send(s, message)
    if response == b'CLOSE':
        print('Connection closed')
        break
    print("Response to M is: ", response)
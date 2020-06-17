import socket
from _thread import *
import threading


class Server:

    def __init__(self, options):
        self.options = options
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.print_lock = threading.Lock()
        self.port = 1212
        self.soc.bind(('', self.port))
        print("socket binded to port", self.port)

    # TO-DO: Define format of data to be accepted by server.
    # TO-DO: Handle and confirm encoding of socket data sent from C/C++/Java.

    def threaded(self, c):
        while True:
            data = c.recv(1024)
            if not data:
                print('Bye')
                self.print_lock.release()
                break
            data = data[::-1]
            c.send(data)
        c.close()

    def socket_listen(self):
        self.soc.listen(5)
        print("socket is listening")

        while True:
            c, addr = self.soc.accept()
            self.print_lock.acquire()
            print('Connected to :', addr[0], ':', addr[1])
            # Start a new thread and return its identifier
            start_new_thread(self.threaded(c))
        self.soc.close()

    def get_user_options(self):
        return self.options.known

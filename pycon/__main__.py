import sys
from app.server import *
from app.options import *


def run(args):
    options = Options()
    options.parse(args[1:])
    server = Server(options)
    server.socket_listen()


if __name__ == '__main__':
    run(sys.argv)

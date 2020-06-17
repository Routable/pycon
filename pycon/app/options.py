from argparse import ArgumentParser


class Options:

    def __init__(self):
        self._init_parser()

    # overrides usage that is by default something like:
    # usage: PROG [-h] [--foo [FOO]] bar [bar ...]
    def _init_parser(self):
        usage = './bin/run_project'
        self.parser = ArgumentParser(usage=usage)

        self.parser.add_argument(
            '-d',
            '--dev',
            default='false',
            dest='development',
            help='Runs pycon in development mode by passing a boolean.')

        self.parser.add_argument(
            '-p',
            '--port',
            default='0.0.0.0',
            dest='port',
            help='Set running port. eg) python3 __main__.py -p 1234')

        self.parser.add_argument(
            '-i',
            '--ip',
            default='127.0.0.1',
            dest='ip',
            help='Set the active IP. eg) python3 main.py -p 192.168.0.1')

    def parse(self, args=None):
        self.known, self.unknown = self.parser.parse_known_args(args)[:]
        if len(self.unknown) != 0:
            print('*WARN* Unknown args received: ' + repr(self.unknown))

import sys
from lib.project import *
from lib.options import *

def run_project(args):
    options = Options()
    options.parse(args[1:])
    project = Project(options)
    print('Printing date:', project.date())
    
    # Preliminary setup to tun application based off of parameters given to application.
    print('Printing example arg:', project.get_user_options())

if __name__ == '__main__':
    run_project(sys.argv)
import sys
from .classmodule import MyClass
from .funcmodule import my_function

def creat(what, *args):
    if what == 'indicador':
        print('create ind', args)       

def main():
    print('main')
    cmd = sys.argv[1]
    args = sys.argv[2:]
    
    if cmd == 'create':
        creat(cmd, *args)
    
if __name__ == '__main__':
    main()
    
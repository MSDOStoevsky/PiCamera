#/usr/bin/python
"""
Python 2.7.15rc1
"""
import util, sys

def main(arg):
    for i in range(arg):
        util.start_camera(i)

if __name__ == "__main__":
    main(int(sys.argv[1]))
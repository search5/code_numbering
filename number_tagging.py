__author__ = 'jiho'

import sys

def main(argv, start_num=0):
    src_file_line_count = bufcount(argv)

    src_file = open(argv, "r")
    out_file = None

    src_num_length = len(str(src_file_line_count))
    line_num_format = "{0:0" + str(src_num_length) + "}: {1}"

    for num, line in enumerate(src_file):
        print(line_num_format.format((num + start_num) + 1, line.rstrip()))

    src_file.close()

def bufcount(filename):
    f = open(filename)
    lines = 1
    buf_size = 1024 * 1024
    read_f = f.read # loop optimization

    buf = read_f(buf_size)
    while buf:
        lines += buf.count('\n')
        buf = read_f(buf_size)

    return lines

if __name__ == "__main__":
    start_num = 0
    if len(sys.argv) == 3:
        start_num = int(sys.argv[2])
    main(sys.argv[1], start_num)
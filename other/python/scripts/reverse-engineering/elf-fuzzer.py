#!/usr/bin/python3

# 17. July 2022

import random
import os

# ./hello > original.out
# echo disas main | gdb ./hello  -q > original.gdb

in_file = './hello'
out_file = './hello_fuzzed'


def fuzz_byte(in_bytes):
    i = random.randint(0, len(in_bytes) - 1)
    c = chr(random.randint(0, 255))
    b = bytes(c, 'utf-8')
    return in_bytes[:i] + b + in_bytes[i + 1:]


def copy_binary():
    with open(in_file, 'rb') as in_f:
        with open(out_file, 'wb') as out_f:
            out_f.write(fuzz_byte(in_f.read()))


def compareFiles(fn1, fn2):
    with open(fn1, 'rb') as f1:
        with open(fn2, 'rb') as f2:
            return f1.read() == f2.read()


def check_output():
    os.system("./hello_fuzzed > fuzzed.out")
    return compareFiles("original.out", "fuzzed.out")


def check_gdb():
    os.system("echo disas main | gdb ./hello_fuzzed -q > fuzzed.gdb")
    return compareFiles("original.gdb", "fuzzed.gdb")


while True:
    copy_binary()
    if check_output() and not check_gdb():
        print("FOUND POSSIBLE FAILURE")
        os.system("tail -n 10 fuzzed.gdb")
        # if fuzzed.gdb first line is (gdb) (gdb) quit, gdb failed
        with open("fuzzed.gdb", 'r') as f:
            if "quit" in f.readline():
                print("GDB FAILED")
                break
        # if previous check is not reliable, try manual review
        # input()  # halt execution until user presses a key
    else:
        print("Failed")
        continue

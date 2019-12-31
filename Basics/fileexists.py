# This file is an exercise on decorators

import os


def exists(old_func):
    def inside(filename):
        if os.path.exists(filename):
            old_func(filename)
        else:
            print("The file does not exist.")

    return inside

@exists
def output_line(input_file):
    with open(input_file) as f:
        print(f.readlines())


output_line("fileexists.py")
output_line("filedoesnotexist.py")

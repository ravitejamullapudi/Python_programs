__author__ = 'Kalyan'

notes = '''
This assignment covers file io and data generation. Actually open the files and check if they are as expected.
'''

from placeholders import *

# Create a text file with name filename and about size bytes. The file should contain
# an incrementing number on each line starting with 0. (ie) 0, 1, 2, 3, .... as many are required to make the file size
# just >= size. Each line should end with windows newline ("\r\n").
def create_file_numbers(filename, size):
    pass

def check_file_size(filename, size):
    import os
    assert os.stat(filename).st_size >= size, "Size not correct"
    f = open(filename, "rb")
    f.seek(size, 0)
    extra = f.read()
    assert extra.count("\r\n") <= 1, "too many extra lines"

def check_file_contents(filename):
    expected_value = 0
    for line in open(filename, "rb"):
        assert line.endswith("\r\n")
        assert expected_value == int(line)
        expected_value += 1


def get_file_path(file):
    import inspect, os.path
    mod_file = inspect.getfile(inspect.currentframe())
    mod_dir = os.path.dirname(mod_file)
    return os.path.join(mod_dir, file)


def test_create_file_numbers():
    file1k =  get_file_path("1k_numbers.txt")
    create_file_numbers(file1k, 1024)
    check_file_size(file1k, 1024)
    check_file_contents(file1k)

    file1M = get_file_path("1M_numbers.txt")
    create_file_numbers(file1M, 1024*1024)
    check_file_size(file1M, 1024*1024)
    check_file_contents(file1M)


three_things_i_learnt = """
-
-
-
"""

time_taken_minutes = ___

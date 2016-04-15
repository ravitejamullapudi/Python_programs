__author__ = 'Kalyan'

notes = '''
This assignment requires you to implement a disk based sort algorithm where not all the data can fit into main memory.
The problem is for you to sort a 2G file using no more than 500 MB of main memory.

http://en.wikipedia.org/wiki/External_sorting
'''

# sorts the input file in ascending order and puts it in the output file. both of them are text files with a
# number on each line.
def disk_sort(input, output):
    pass


# generate test data in the file so that the file is of specified size (as in previous assignment).
# every line in the text file is a random number between 1 and 1000,000
def generate_test_data(file, size):
    pass


def check_output(output):
    previous_value = 0
    for line in open(output, "rb"):
        assert line.endswith("\r\n")
        current_value = int(line)
        assert current_value >= previous_value
        previous_value = current_value

def get_file_path(file):
    import inspect, os.path
    mod_file = inspect.getfile(inspect.currentframe())
    mod_dir = os.path.dirname(mod_file)
    return os.path.join(mod_dir, file)

def test_disk_sort():
    input_path = get_file_path("input")
    output_path = get_file_path("output")
    generate_test_data(input_path, 2*1024*1024*1024)
    disk_sort(input_path, output_path)
    check_output(output_path)




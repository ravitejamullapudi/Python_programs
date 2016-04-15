__author__ = 'Kalyan'

notes = '''
For this exercise, you are going to do 2 things that you typically do in a job -

 - picking tools that do want you want and then figuring out how to install and use them (google search, product
   documentation, stack overflow etc.).
 - performance measurements of some behavior as you scale some parameter.


1. The tool you must install and use is pygal - a charting module for python.
2. Create a line chart for the file write performance of the program you have written in the previous assignment for
   various values of buffers you can pass to open function.
   buffer values are scaled across 0, 1, 1k, 2k, 4k, 8k and
   file size values are 1k, 10k, 100k, 1m, 10m, 20m

This is a free form assignment, so you need to fill up the code below. It will include your code to generate the file of
given size and the code to generate the chart. It must generate a 'io-perf.svg' file in the module directory.
'''

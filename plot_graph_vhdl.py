import argparse
import os
from GraphVhdl import parse_file

parser = argparse.ArgumentParser()
parser.add_argument("vhdl_file", help="top-level synthesizable file")
# parser.add_argument("-d", "--directory",
#                    type=str, default=".",
#                    help="directory where to search for components")
# parser.add_argument("-o", "--output",
#                    type=str, default="GraphVhdl.png",
#                    help="name of output file")

vhdl_file = parser.parse_args().vhdl_file
file_path = os.path.join(os.getcwd(), vhdl_file)
print(file_path)
print(parse_file(file_path).instances_list)

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("TOP-LEVEL", help="top-level synthesizable file")
parser.add_argument("-d", "--directory",
                    type=str, default=".",
                    help="directory where to search for components")
parser.add_argument("-o", "--output",
                    type=str, default="GraphVhdl.png",
                    help="name of output file")
parser.parse_args()

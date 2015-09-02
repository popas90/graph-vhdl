import sys
from antlr4 import *
from vhdlLexer import vhdlLexer
from vhdlParser import vhdlParser
from vhdlListener import vhdlListener
 
def main(argv):
    input = FileStream(argv[1])
    lexer = vhdlLexer(input)
    stream = CommonTokenStream(lexer)
    parser = vhdlParser(stream)
    listener = vhdlListener()
    tree = parser.design_file()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
 
if __name__ == '__main__':
    main(sys.argv)
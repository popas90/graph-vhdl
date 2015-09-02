import sys
from antlr4 import *
from VhdlLexer import VhdlLexer
from VhdlParser import VhdlParser
from VhdlListener import VhdlListener
 
def main(argv):
    input = FileStream(argv[1])
    lexer = VhdlLexer(input)
    stream = CommonTokenStream(lexer)
    parser = VhdlParser(stream)
    listener = VhdlListener()
    tree = parser.design_file()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
 
if __name__ == '__main__':
    main(sys.argv)
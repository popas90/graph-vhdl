import sys
from antlr4 import *
from VhdlLexer import VhdlLexer
from VhdlParser import VhdlParser
from VhdlListenerForGraph import VhdlListenerForGraph
from VhdlVisitorForGraph import VhdlVisitorForGraph
 
def main(argv):
    input = FileStream(argv[1])
    lexer = VhdlLexer(input)
    stream = CommonTokenStream(lexer)
    parser = VhdlParser(stream)
    parser._interp.predictionMode = PredictionMode.SLL
    listener = VhdlListenerForGraph()
    try:
        print("Trying with SLL...")
        tree = parser.design_file()
    except:
        print("SLL didn't work...")
        stream.reset()
        parser.reset()
        parser._interp.predictionMode = PredictionMode.LL
        tree = parser.design_file()
    finally:
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
    #grapher = VhdlVisitorForGraph()
    #grapher.visit(tree)

 
if __name__ == '__main__':
    main(sys.argv)
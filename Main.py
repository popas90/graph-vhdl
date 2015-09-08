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
    parser._interp.predictionMode = PredictionMode.LL
    listener = VhdlListenerForGraph()
    try:
        print("Parsing with SLL...")
        tree = parser.design_file()
    except:
        print("SLL didn't work, parsing with LL...")
        stream.reset()
        parser.reset()
        parser._interp.predictionMode = PredictionMode.LL
        tree = parser.design_file()
    finally:
        print("Done parsing, walking parse tree...")
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
    #grapher = VhdlVisitorForGraph()
    #grapher.visit(tree)

 
if __name__ == '__main__':
    main(sys.argv)
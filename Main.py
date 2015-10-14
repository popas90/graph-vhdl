import sys
from antlr4 import *
from antlr_generated.VhdlLexer import VhdlLexer
from antlr_generated.VhdlParser import VhdlParser
from VhdlListenerForGraph import VhdlListenerForGraph


def main(argv):
    input = FileStream(argv[1])
    lexer = VhdlLexer(input)
    stream = CommonTokenStream(lexer)
    parser = VhdlParser(stream)
    listener = VhdlListenerForGraph()
    parser_option = argv[2]

    if (parser_option == "SLL"):
        parser._interp.predictionMode = PredictionMode.SLL
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
    elif (parser_option == "LL"):
        print("Parsing with LL...")
        parser._interp.predictionMode = PredictionMode.LL
        tree = parser.design_file()
        print("Done parsing, walking parse tree...")
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

    print(len(listener.components_list))

    # grapher = VhdlVisitorForGraph()
    # grapher.visit(tree)


if __name__ == '__main__':
    main(sys.argv)

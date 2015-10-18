from antlr4 import *
from antlr_generated.VhdlLexer import VhdlLexer
from antlr_generated.VhdlParser import VhdlParser
from VhdlListenerForGraph import VhdlListenerForGraph
import nose


def test_identify_instances():
    inp = FileStream('./tests/testfiles/struct_with_components.vhd')
    lexer = VhdlLexer(inp)
    stream = CommonTokenStream(lexer)
    parser = VhdlParser(stream)
    listener = VhdlListenerForGraph()
    parser._interp.predictionMode = PredictionMode.LL
    tree = parser.design_file()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    nose.tools.eq_(len(listener.components_list), 2)


def test_no_instances():
    inp = FileStream('./tests/testfiles/d_flop_behav.vhd')
    lexer = VhdlLexer(inp)
    stream = CommonTokenStream(lexer)
    parser = VhdlParser(stream)
    listener = VhdlListenerForGraph()
    parser._interp.predictionMode = PredictionMode.LL
    tree = parser.design_file()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    nose.tools.eq_(len(listener.components_list), 0)

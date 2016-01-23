from antlr4 import *
from antlr_generated.VhdlLexer import VhdlLexer
from antlr_generated.VhdlParser import VhdlParser
from VhdlListenerForGraph import VhdlListenerForGraph
import nose


def parse_file_setup(file_path):
    inp = FileStream(file_path)
    lexer = VhdlLexer(inp)
    stream = CommonTokenStream(lexer)
    parser = VhdlParser(stream)
    listener = VhdlListenerForGraph()
    parser._interp.predictionMode = PredictionMode.LL
    tree = parser.design_file()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return listener


def test_identify_instances():
    listener = parse_file_setup('./tests/testfiles/struct_with_components.vhd')
    nose.tools.eq_(len(listener.instances_list), 2)


def test_no_instances():
    listener = parse_file_setup('./tests/testfiles/d_flop_behav.vhd')
    nose.tools.eq_(len(listener.instances_list), 0)


def test_one_process():
    listener = parse_file_setup('./tests/testfiles/ac_behave.vhd')
    nose.tools.eq_(len(listener.processes_list), 1)

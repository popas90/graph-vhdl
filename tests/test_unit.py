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


def test_two_instances():
    listener = parse_file_setup('./tests/testfiles/struct_with_components.vhd')
    nose.tools.eq_(len(listener.instances_list), 2)
    nose.tools.eq_(listener.instances_list[0].name, 'xor2')
    nose.tools.eq_(listener.instances_list[0].label, 'u0')
    nose.tools.eq_(listener.instances_list[0].associations, [])
    nose.tools.eq_(listener.instances_list[1].name, 'inv')
    nose.tools.eq_(listener.instances_list[1].label, 'u1')


def test_zero_instances():
    listener = parse_file_setup('./tests/testfiles/d_flop_behav.vhd')
    nose.tools.eq_(len(listener.instances_list), 0)


def test_one_process():
    listener = parse_file_setup('./tests/testfiles/ac_behave.vhd')
    nose.tools.eq_(len(listener.processes_list), 1)
    nose.tools.eq_(listener.processes_list[0].label, 'main')


def test_zero_processes():
    listener = parse_file_setup('./tests/testfiles/struct_with_components.vhd')
    nose.tools.eq_(len(listener.processes_list), 0)

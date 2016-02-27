from antlr4 import *
from antlr_generated.VhdlLexer import VhdlLexer
from antlr_generated.VhdlParser import VhdlParser
from VhdlListenerForGraph import VhdlListenerForGraph
from vhdl_model.Association import Association
from utilities.DataObject import DataObject
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
    port_map0 = [Association("a"), Association("b"), Association("tmp")]
    port_map1 = [Association("tmp"), Association("c")]
    nose.tools.eq_(len(listener.instances_list), 2)
    nose.tools.eq_(listener.instances_list[0].name, 'xor2')
    nose.tools.eq_(listener.instances_list[0].label, 'u0')
    nose.tools.eq_(listener.instances_list[0].generic_map, None)
    nose.tools.eq_(listener.instances_list[0].port_map.elements, port_map0)
    nose.tools.eq_(listener.instances_list[1].name, 'inv')
    nose.tools.eq_(listener.instances_list[1].label, 'u1')
    nose.tools.eq_(listener.instances_list[1].generic_map, None)
    nose.tools.eq_(listener.instances_list[1].port_map.elements, port_map1)


def test_zero_instances():
    listener = parse_file_setup('./tests/testfiles/d_flop_behav.vhd')
    nose.tools.eq_(len(listener.instances_list), 0)


def test_one_process():
    listener = parse_file_setup('./tests/testfiles/ac_behave.vhd')
    sensitivity_list = {'clr', 'clk', 'la', 'ea', 'd'}
    outputs_list = {'q_data', 'q_alu'}
    inputs_list = {'d', 'ea'}
    nose.tools.eq_(len(listener.processes_list), 1)
    nose.tools.eq_(listener.processes_list[0].label, 'main')
    nose.tools.eq_(listener.processes_list[0].sensitivity_list,
                   sensitivity_list)
    nose.tools.eq_(listener.processes_list[0].outputs, outputs_list)
    nose.tools.eq_(listener.processes_list[0].inputs, inputs_list)


def test_zero_processes():
    listener = parse_file_setup('./tests/testfiles/struct_with_components.vhd')
    nose.tools.eq_(len(listener.processes_list), 0)

from antlr4 import *
from antlr_generated.VhdlListener import VhdlListener
from vhdl_model.Component import Component
from vhdl_model.Process import Process
from utilities.Deque import Deque
from utilities.DataObject import DataObject
from collections import namedtuple
import logging


class VhdlListenerForGraph(VhdlListener):

    def __init__(self):
        logging.basicConfig(filename='runtime.log',
                            filemode='w',
                            level=logging.DEBUG)
        self.parsing_stack = Deque(logging=True)
        # TODO maybe a hashmap would be better here ?
        self.instances_list = []
        self.processes_list = []

    # component_instantiation_statement
    def enterComponent_instantiation_statement(self, ctx):
        self.parsing_stack.push(Component())

    def exitComponent_instantiation_statement(self, ctx):
        self.instances_list.append(self.parsing_stack.pop())

    # label_colon
    def enterLabel_colon(self, ctx):
        self.parsing_stack.push(DataObject('Label'))

    def exitLabel_colon(self, ctx):
        label = self.parsing_stack.pop()
        self.parsing_stack.preview_top().add_label(label.identifier)

    # instantiated_unit
    def enterInstantiated_unit(self, ctx):
        self.parsing_stack.push(DataObject('InstantiatedUnit'))

    def exitInstantiated_unit(self, ctx):
        instantiated_unit = self.parsing_stack.pop()
        self.parsing_stack.preview_top().add_name(instantiated_unit.identifier)

    # name
    def enterName(self, ctx):
        self.parsing_stack.push(DataObject('Name'))

    def exitName(self, ctx):
        name = self.parsing_stack.pop()
        self.parsing_stack.preview_top().identifier = name.identifier

    # identifier
    def enterIdentifier(self, ctx):
        top = self.parsing_stack.preview_top()
        if hasattr(top, 'identifier'):
            top.identifier = ctx.BASIC_IDENTIFIER()

    def exitIdentifier(self, ctx):
        pass

    # port_map_aspect
    def enterPort_map_aspect(self, ctx):
        self.parsing_stack.push(DataObject('PortMap'))
        self.parsing_stack.preview_top().associations = []

    def exitPort_map_aspect(self, ctx):
        port_map = self.parsing_stack.pop()
        # TODO add port_map property to Component as a list of associations
        self.parsing_stack.preview_top().port_map = port_map

    # association_element
    def enterAssociation_element(self, ctx):
        self.parsing_stack.push(namedtuple("Association",
                                           ["formal", "actual"]))

    def exitAssociation_element(self, ctx):
        association = self.parsing_stack.pop()
        if isinstance(self.parsing_stack.preview_top(), Component):
            self.parsing_stack.preview_top().associations.append(association)

    # formal_part
    def enterFormal_part(self, ctx):
        self.parsing_stack.push(DataObject('Formal'))

    def exitFormal_part(self, ctx):
        formal_part = self.parsing_stack.pop()
        self.parsing_stack.preview_top().formal = formal_part.identifier

    # actual_part
    def enterActual_part(self, ctx):
        self.parsing_stack.push(DataObject('Actual'))

    def exitActual_part(self, ctx):
        actual_part = self.parsing_stack.pop()
        self.parsing_stack.preview_top().actual = actual_part.identifier

    # process_statement
    def enterProcess_statement(self, ctx):
        self.parsing_stack.push(Process())

    def exitProcess_statement(self, ctx):
        self.processes_list.append(self.parsing_stack.pop())

    # sensitivity_list
    def enterSensitivity_list(self, ctx):
        pass

    def exitSensitivity_list(self, ctx):
        pass

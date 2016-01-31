from antlr4 import *
from antlr_generated.VhdlListener import VhdlListener
from vhdl_model.Component import Component
from vhdl_model.Process import Process
from utilities.Deque import Deque
from utilities.DataObject import DataObject
from collections import namedtuple
from collections import deque
import logging


class VhdlListenerForGraph(VhdlListener):

    def __init__(self):
        logging.basicConfig(filename='runtime.log',
                            filemode='w',
                            level=logging.DEBUG)
        self.parsing_stack = deque()  # Deque(logging=True)
        # TODO maybe a hashmap would be better here ?
        self.instances_list = []
        self.processes_list = []

    def pop(self):
        return self.parsing_stack.pop()

    def peek(self):
        if len(self.parsing_stack) == 0:
            return None
        else:
            return self.parsing_stack[-1]

    def push(self, new_elem):
        self.parsing_stack.append(new_elem)

    # component_instantiation_statement
    def enterComponent_instantiation_statement(self, ctx):
        self.push(Component())

    def exitComponent_instantiation_statement(self, ctx):
        self.instances_list.append(self.pop())

    # instantiated_unit
    def enterInstantiated_unit(self, ctx):
        self.push(DataObject('InstantiatedUnit'))

    def exitInstantiated_unit(self, ctx):
        instantiated_unit = self.pop()
        self.peek().name = instantiated_unit.identifier

    # name
    def enterName(self, ctx):
        self.push(DataObject('Name'))

    def exitName(self, ctx):
        name = self.pop()
        self.peek().identifier = name.identifier

    # label_colon
    def enterLabel_colon(self, ctx):
        self.push(DataObject('Label'))

    def exitLabel_colon(self, ctx):
        label = self.pop()
        self.peek().label = label.identifier

    # identifier
    def enterIdentifier(self, ctx):
        top = self.peek()
        if hasattr(top, 'identifier'):
            top.identifier = str(ctx.BASIC_IDENTIFIER())

    def exitIdentifier(self, ctx):
        pass

    # port_map_aspect
    def enterPort_map_aspect(self, ctx):
        self.push(DataObject('PortMap'))
        self.peek().associations = []

    def exitPort_map_aspect(self, ctx):
        port_map = self.pop()
        # TODO add port_map property to Component as a list of associations
        self.peek().port_map = port_map

    # association_element
    def enterAssociation_element(self, ctx):
        self.push(namedtuple("Association", ["formal", "actual"]))

    def exitAssociation_element(self, ctx):
        association = self.pop()
        if isinstance(self.peek(), Component):
            self.peek().associations.append(association)

    # formal_part
    def enterFormal_part(self, ctx):
        self.push(DataObject('Formal'))

    def exitFormal_part(self, ctx):
        formal_part = self.pop()
        self.peek().formal = formal_part.identifier

    # actual_part
    def enterActual_part(self, ctx):
        self.push(DataObject('Actual'))

    def exitActual_part(self, ctx):
        actual_part = self.pop()
        self.peek().actual = actual_part.identifier

    # process_statement
    def enterProcess_statement(self, ctx):
        self.push(Process())

    def exitProcess_statement(self, ctx):
        self.processes_list.append(self.pop())

    # sensitivity_list
    def enterSensitivity_list(self, ctx):
        pass

    def exitSensitivity_list(self, ctx):
        pass

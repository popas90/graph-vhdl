from antlr4 import *
from antlr_generated.VhdlListener import VhdlListener
from vhdl_model.Instance import Instance
from vhdl_model.Process import Process
from vhdl_model.Association import Association
from utilities.Deque import Deque
from utilities.DataObject import DataObject
from utilities.DataContainer import DataContainer
from collections import namedtuple
from collections import deque
import logging


class VhdlListenerForGraph(VhdlListener):

    def __init__(self):
        logging.basicConfig(filename='runtime.log',
                            filemode='w',
                            level=logging.INFO)
        self.parsing_stack = Deque(logging=True)  # deque()
        # TODO maybe a hashmap would be better here ?
        self.instances_list = []
        self.processes_list = []

    def pop(self):
        return self.parsing_stack.pop()

    def peek(self):
        return self.parsing_stack.preview_top()

    def push(self, new_elem):
        self.parsing_stack.push(new_elem)

    # Component_instantiation_statement
    def enterComponent_instantiation_statement(self, ctx):
        self.push(Instance())

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
        top = self.peek()
        if isinstance(top, DataObject):
            self.peek().identifier = name.identifier
        if isinstance(top, DataContainer):
            self.peek().elements.append(name)

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

    # generic_map_aspect
    def enterGeneric_map_aspect(self, ctx):
        self.push(DataContainer('GenericMap'))

    def exitGeneric_map_aspect(self, ctx):
        generic_map = self.pop()
        self.peek().generic_map = generic_map

    # port_map_aspect
    def enterPort_map_aspect(self, ctx):
        self.push(DataContainer('PortMap'))

    def exitPort_map_aspect(self, ctx):
        port_map = self.pop()
        self.peek().port_map = port_map

    # association_element
    def enterAssociation_element(self, ctx):
        # self.push(namedtuple("Association", ["formal", "actual"]))
        self.push(Association())

    def exitAssociation_element(self, ctx):
        association = self.pop()
        if isinstance(self.peek(), DataContainer):
            self.peek().elements.append(association)

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
        self.push(DataContainer("Sensitivity_list"))

    def exitSensitivity_list(self, ctx):
        sensitivity_list = self.pop()
        self.peek().sensitivity_list = sensitivity_list

    # target
    def enterTarget(self, ctx):
        self.push(DataObject('Target'))

    def exitTarget(self, ctx):
        target = self.pop()
        self.peek().outputs.add(target)

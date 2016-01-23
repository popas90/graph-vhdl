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
        # Create an empty Component instance and add it to the parsing stack
        self.parsing_stack.push(Component())
        # logging.info("PUSH Component")

    def exitComponent_instantiation_statement(self, ctx):
        # Pop the parsing stack and add the element to the components list
        self.instances_list.append(self.parsing_stack.pop())
        # logging.info("POP  Component")

    # label_colon
    def enterLabel_colon(self, ctx):
        self.parsing_stack.push(DataObject('Label'))
        # logging.info("PUSH Label")

    def exitLabel_colon(self, ctx):
        label = self.parsing_stack.pop()
        self.parsing_stack.preview_top().add_label(label.identifier)
        # logging.info("POP  Label")

    # instantiated_unit
    def enterInstantiated_unit(self, ctx):
        self.parsing_stack.push(DataObject('InstantiatedUnit'))
        # logging.info("PUSH InstantiatedUnit")

    def exitInstantiated_unit(self, ctx):
        instantiated_unit = self.parsing_stack.pop()
        self.parsing_stack.preview_top().add_name(instantiated_unit.identifier)
        # logging.info("POP  InstantiatedUnit")

    # name
    def enterName(self, ctx):
        self.parsing_stack.push(DataObject('Name'))
        # logging.info("PUSH Name")

    def exitName(self, ctx):
        name = self.parsing_stack.pop()
        # For now, assume it's an instantiated unit
        # if isinstance(self.parsing_stack.preview_top(), tuple):
        self.parsing_stack.preview_top().identifier = name.identifier
        # logging.info("POP  Name")

    # identifier
    def enterIdentifier(self, ctx):
        # print(ctx.BASIC_IDENTIFIER())
        top = self.parsing_stack.preview_top()
        if hasattr(top, 'identifier'):
            top.identifier = ctx.BASIC_IDENTIFIER()
        # logging.info("SET  identifier {}".format(ctx.BASIC_IDENTIFIER()))

    def exitIdentifier(self, ctx):
        pass

    # port_map_aspect
    def enterPort_map_aspect(self, ctx):
        self.parsing_stack.push(DataObject('PortMap'))
        self.parsing_stack.preview_top().associations = []
        # logging.info("PUSH PortMap")

    def exitPort_map_aspect(self, ctx):
        port_map = self.parsing_stack.pop()
        # TODO add port_map property to Component as a list of associations
        self.parsing_stack.preview_top().port_map = port_map
        # logging.info("POP  PortMap")

    # association_element
    def enterAssociation_element(self, ctx):
        self.parsing_stack.push(namedtuple("Association",
                                           ["formal", "actual"]))
        # logging.info("PUSH Association")

    def exitAssociation_element(self, ctx):
        association = self.parsing_stack.pop()
        if isinstance(self.parsing_stack.preview_top(), Component):
            self.parsing_stack.preview_top().associations.append(association)
        # logging.info("POP  Association")

    # formal_part
    def enterFormal_part(self, ctx):
        self.parsing_stack.push(DataObject('Formal'))
        # logging.info("PUSH Formal")

    def exitFormal_part(self, ctx):
        formal_part = self.parsing_stack.pop()
        self.parsing_stack.preview_top().formal = formal_part.identifier
        # logging.info("POP  Formal")

    # actual_part
    def enterActual_part(self, ctx):
        self.parsing_stack.push(DataObject('Actual'))
        # logging.info("PUSH actual_part")

    def exitActual_part(self, ctx):
        actual_part = self.parsing_stack.pop()
        self.parsing_stack.preview_top().actual = actual_part.identifier
        # logging.info("POP  actual_part")

    # process_statement
    def enterProcess_statement(self, ctx):
        self.parsing_stack.push(Process())
        # logging.info("PUSH process_statement")

    def exitProcess_statement(self, ctx):
        self.processes_list.append(self.parsing_stack.pop())
        # logging.info("POP  process_statement")

    # sensitivity_list
    def enterSensitivity_list(self, ctx):
        pass

    def exitSensitivity_list(self, ctx):
        pass

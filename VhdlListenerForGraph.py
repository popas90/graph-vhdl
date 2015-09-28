from antlr4 import *
from VhdlListener import VhdlListener
from VhdlParser import VhdlParser
from Component import Component
from Deque import Deque
from collections import namedtuple
import logging


# This class defines a complete listener for a parse tree produced by VhdlParser.
class VhdlListenerForGraph(VhdlListener):

    def __init__(self):
        logging.basicConfig(filename='runtime.log', filemode='w', level=logging.DEBUG)
        self.parsing_stack = Deque()
        # TODO maybe a hashmap would be better here ?
        self.components_list = []

    # Component instantiation statement
    def enterComponent_instantiation_statement(self, ctx:VhdlParser.Component_instantiation_statementContext):
        # Create an empty Component instance and add it to the parsing stack
        self.parsing_stack.push(Component())
        logging.info("PUSH Component")

    def exitComponent_instantiation_statement(self, ctx:VhdlParser.Component_instantiation_statementContext):
        # Pop the parsing stack and add the element to the components list
        self.components_list.append(self.parsing_stack.pop())
        logging.info("POP  Component")

    # Label colon
    def enterLabel_colon(self, ctx:VhdlParser.Label_colonContext):
        self.parsing_stack.push(namedtuple("Label", "identifier"))
        logging.info("PUSH Label")

    def exitLabel_colon(self, ctx:VhdlParser.Label_colonContext):
        label = self.parsing_stack.pop()
        self.parsing_stack.preview_top().add_label(label.identifier)
        logging.info("POP  Label")

    # Instantiation unit
    def enterInstantiated_unit(self, ctx:VhdlParser.Instantiated_unitContext):
        self.parsing_stack.push(namedtuple("InstantiatedUnit", "identifier"))
        logging.info("PUSH InstantiatedUnit")

    def exitInstantiated_unit(self, ctx:VhdlParser.Instantiated_unitContext):
        instantiated_unit = self.parsing_stack.pop()
        self.parsing_stack.preview_top().add_name(instantiated_unit.identifier)
        logging.info("POP  InstantiatedUnit")

    # Name
    def enterName(self, ctx:VhdlParser.NameContext):
        self.parsing_stack.push(namedtuple("Name", "identifier"))
        logging.info("PUSH Name")

    def exitName(self, ctx:VhdlParser.NameContext):
        name = self.parsing_stack.pop()
        # For now, assume it's an instantiated unit
        self.parsing_stack.preview_top().identifier = name.identifier
        logging.info("POP  Name")

    # Identifier
    def enterIdentifier(self, ctx:VhdlParser.IdentifierContext):
        #self.parsing_stack.preview_top().identifier = ctx.BASIC_IDENTIFIER()
        logging.info("SET  identifier {}".format(ctx.BASIC_IDENTIFIER()))

    def exitIdentifier(self, ctx:VhdlParser.IdentifierContext):
        pass

    # Port map aspect
    def enterPort_map_aspect(self, ctx:VhdlParser.Port_map_aspectContext):
        self.parsing_stack.push(namedtuple("PortMap", "associations"))
        self.parsing_stack.preview_top().associations = []
        logging.info("PUSH PortMap")

    def exitPort_map_aspect(self, ctx:VhdlParser.Port_map_aspectContext):
        port_map = self.parsing_stack.pop()
        # TODO add port_map property to Component as a list of associations
        self.parsing_stack.preview_top().port_map = port_map
        logging.info("POP  PortMap")

    # Association element
    def enterAssociation_element(self, ctx:VhdlParser.Association_elementContext):
        self.parsing_stack.push(namedtuple("Association", ["formal", "actual"]))
        logging.info("PUSH Association")

    def exitAssociation_element(self, ctx:VhdlParser.Association_elementContext):
        association = self.parsing_stack.pop()
        self.parsing_stack.preview_top().associations.append(association)
        logging.info("POP  Association")

    # Formal part
    def enterFormal_part(self, ctx:VhdlParser.Formal_partContext):
        self.parsing_stack.push(namedtuple("Formal", "identifier"))
        logging.info("PUSH Formal")

    def exitFormal_part(self, ctx:VhdlParser.Formal_partContext):
        formal_part = self.parsing_stack.pop()
        self.parsing_stack.preview_top().formal = formal_part.identifier
        logging.info("POP  Formal")

    # Actual part
    def enterActual_part(self, ctx:VhdlParser.Actual_partContext):
        self.parsing_stack.push(namedtuple("Actual", "identifier"))
        logging.info("PUSH Actual")

    def exitActual_part(self, ctx:VhdlParser.Actual_partContext):
        actual_part = self.parsing_stack.pop()
        self.parsing_stack.preview_top().actual = actual_part.identifier
        logging.info("POP  Actual")

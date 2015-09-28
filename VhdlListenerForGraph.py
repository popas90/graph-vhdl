from antlr4 import *
from VhdlListener import VhdlListener
from VhdlParser import VhdlParser
from Component import Component
from Deque import Deque
from collections import namedtuple


# This class defines a complete listener for a parse tree produced by VhdlParser.
class VhdlListenerForGraph(VhdlListener):

    def __init__(self):
        self.parsing_stack = Deque()
        # TODO maybe a hashmap would be better here ?
        self.components_list = []

    # Component instantiation statement
    def enterComponent_instantiation_statement(self, ctx:VhdlParser.Component_instantiation_statementContext):
        # Create an empty Component instance and add it to the parsing stack
        self.parsing_stack.push(Component())

    def exitComponent_instantiation_statement(self, ctx:VhdlParser.Component_instantiation_statementContext):
        # Pop the parsing stack and add the element to the components list
        self.components_list.append(self.parsing_stack.pop())

    # Label colon
    def enterLabel_colon(self, ctx:VhdlParser.Label_colonContext):
        self.parsing_stack.push(namedtuple("Label", "identifier"))

    def exitLabel_colon(self, ctx:VhdlParser.Label_colonContext):
        label = self.parsing_stack.pop()
        self.parsing_stack.preview_top().set_label(label.identifier)

    # Instantiation unit
    def enterInstantiated_unit(self, ctx:VhdlParser.Instantiated_unitContext):
        self.parsing_stack.push(namedtuple("InstantiatedUnit", "identifier"))

    def exitInstantiated_unit(self, ctx:VhdlParser.Instantiated_unitContext):
        instantiated_unit = self.parsing_stack.pop()
        self.parsing_stack.preview_top().set_name(instantiated_unit.identifier)

    # Name
    def enterName(self, ctx:VhdlParser.NameContext):
        self.parsing_stack.push(namedtuple("Name", "identifier"))

    def exitName(self, ctx:VhdlParser.NameContext):
        name = self.parsing_stack.pop()
        # TODO see what kind of node this is
        # For now, assume it's an instantiated unit
        self.parsing_stack.preview_top().set_identifier(name.identifier)

    # Identifier
    def enterIdentifier(self, ctx:VhdlParser.IdentifierContext):
        self.parsing_stack.preview_top().identifier = ctx.BASIC_IDENTIFIER()

    def exitIdentifier(self, ctx:VhdlParser.IdentifierContext):
        pass

    # Port map aspect
    def enterPort_map_aspect(self, ctx:VhdlParser.Port_map_aspectContext):
        self.parsing_stack.push(namedtuple("PortMap", "associations"))
        self.parsing_stack.preview_top().associations = []

    def exitPort_map_aspect(self, ctx:VhdlParser.Port_map_aspectContext):
        port_map = self.parsing_stack.pop()
        # TODO add port_map property to Component as a list of associations
        self.parsing_stack.preview_top().port_map = port_map

    # Association element
    def enterAssociation_element(self, ctx:VhdlParser.Association_elementContext):
        self.parsing_stack.push(namedtuple("Association", ["formal", "actual"]))

    def exitAssociation_element(self, ctx:VhdlParser.Association_elementContext):
        association = self.parsing_stack.pop()
        self.parsing_stack.preview_top().associations.push(association)

    # Formal part
    def enterFormal_part(self, ctx:VhdlParser.Formal_partContext):
        self.parsing_stack.push(namedtuple("Formal", "identifier"))

    def exitFormal_part(self, ctx:VhdlParser.Formal_partContext):
        formal_part = self.parsing_stack.pop()
        self.parsing_stack.preview_top().formal = formal_part.identifier

    # Actual part
    def enterActual_part(self, ctx:VhdlParser.Actual_partContext):
        self.parsing_stack.push(namedtuple("Actual", "identifier"))

    def exitActual_part(self, ctx:VhdlParser.Actual_partContext):
        actual_part = self.parsing_stack.pop()
        self.parsing_stack.preview_top().actual = actual_part.identifier

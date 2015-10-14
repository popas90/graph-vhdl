from antlr4 import *
from antlr_generated.VhdlListener import VhdlListener
from antlr_generated.VhdlParser import VhdlParser
from vhdl_model.Component import Component
from Deque import Deque
from vhdl_model.Label import Label
from StringContainer import StringContainer
from StringContainer import StringContainerCategory


# This class defines a complete listener for a parse tree produced by VhdlParser.
class VhdlListenerForGraph(VhdlListener):

    def __init__(self):
        self.parsing_stack = Deque()
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
        self.parsing_stack.push(StringContainer(StringContainerCategory.Label))

    def exitLabel_colon(self, ctx:VhdlParser.Label_colonContext):
        label = self.parsing_stack.pop()
        self.parsing_stack.preview_top().set_label(label.value)

    # Instantiation unit
    def enterInstantiated_unit(self, ctx:VhdlParser.Instantiated_unitContext):
        self.parsing_stack.push(StringContainer(StringContainerCategory.Instantiated_Unit))

    def exitInstantiated_unit(self, ctx:VhdlParser.Instantiated_unitContext):
        instantiated_unit = self.parsing_stack.pop()
        self.parsing_stack.preview_top().set_name(instantiated_unit.value)

    # Name
    def enterName(self, ctx:VhdlParser.NameContext):
        self.parsing_stack.push(StringContainer(StringContainerCategory.Name))

    def exitName(self, ctx:VhdlParser.NameContext):
        name = self.parsing_stack.pop()
        # For now, assume it's an instantiated unit
        if (isinstance(self.parsing_stack.preview_top(), StringContainer) ):
            self.parsing_stack.preview_top().set_identifier(name.value)

    # Identifier
    def enterIdentifier(self, ctx:VhdlParser.IdentifierContext):
        self.parsing_stack.preview_top().set_identifier(ctx.BASIC_IDENTIFIER())

    def exitIdentifier(self, ctx:VhdlParser.IdentifierContext):
        pass

    # Port map aspect
    def enterPort_map_aspect(self, ctx:VhdlParser.Port_map_aspectContext):
        pass

    def exitPort_map_aspect(self, ctx:VhdlParser.Port_map_aspectContext):
        pass

    # Association element
    def enterAssociation_element(self, ctx:VhdlParser.Association_elementContext):
        pass

    def exitAssociation_element(self, ctx:VhdlParser.Association_elementContext):
        pass

    # Formal part
    def enterFormal_part(self, ctx:VhdlParser.Formal_partContext):
        pass

    def exitFormal_part(self, ctx:VhdlParser.Formal_partContext):
        pass

    # Actual part
    def enterActual_part(self, ctx:VhdlParser.Actual_partContext):
        pass

    def exitActual_part(self, ctx:VhdlParser.Actual_partContext):
        pass

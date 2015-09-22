from antlr4 import *
from VhdlListener import VhdlListener
from VhdlParser import VhdlParser
from Component import Component

# This class defines a complete listener for a parse tree produced by VhdlParser.
class VhdlListenerForGraph(VhdlListener):

    def __init__(self):
        # TODO look for a better implem for a stack (preview, push, pop, rpush, rpop)
        self.parsing_stack = []
        self.components_list = []
        self.search_for_instance = False
        self.search_for_port_map = False
        self.in_signal_assignment = False

    # Entering the component instantiation statement
    def enterComponent_instantiation_statement(self, ctx:VhdlParser.Component_instantiation_statementContext):
        # Create an empty Component instance and add it to the parsing stack
        self.parsing_stack.append(Component())

    # Exiting the component instantiation statement
    def exitComponent_instantiation_statement(self, ctx:VhdlParser.Component_instantiation_statementContext):
        # Pop the parsing stack and add the element to the components list
        self.components_list.append(self.parsing_stack.pop())

    # Entering the instantiation_unit rule
    def enterInstantiated_unit(self, ctx:VhdlParser.Instantiated_unitContext):
        pass

    # Exiting the instantiation_unit rule
    def exitInstantiated_unit(self, ctx:VhdlParser.Instantiated_unitContext):
        pass

    # Entering identifier rule
    def enterIdentifier(self, ctx:VhdlParser.IdentifierContext):
        # TODO this should be a dynamic (or to the base class) call to add a name
        self.parsing_stack.preview().add_name()

    # Entering port map rule
    def enterPort_map_aspect(self, ctx:VhdlParser.Port_map_aspectContext):
        self.search_for_port_map = True

    # Exiting port map rule
    def exitPort_map_aspect(self, ctx:VhdlParser.Port_map_aspectContext):
        self.search_for_port_map = False

    # Entering concurrent signal assignment
    def enterConcurrent_signal_assignment_statement(self, ctx:VhdlParser.Concurrent_signal_assignment_statementContext):
        print("...entering signal assignment")
        self.in_signal_assignment = True

    # Exiting concurrent signal assignment
    def exitConcurrent_signal_assignment_statement(self, ctx:VhdlParser.Concurrent_signal_assignment_statementContext):
        print("...exiting signal assignment")
        self.in_signal_assignment = False

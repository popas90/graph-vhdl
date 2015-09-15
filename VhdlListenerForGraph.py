from antlr4 import *
from VhdlListener import VhdlListener
from VhdlParser import VhdlParser

# This class defines a complete listener for a parse tree produced by VhdlParser.
class VhdlListenerForGraph(VhdlListener):

    def __init__(self):
        self.search_for_instance = False
        self.search_for_port_map = False
        self.in_signal_assignment = False

    # Entering the instantiation_unit rule
    def enterInstantiated_unit(self, ctx:VhdlParser.Instantiated_unitContext):
        self.search_for_instance = True

    # Exiting the instantiation_unit rule
    def exitInstantiated_unit(self, ctx:VhdlParser.Instantiated_unitContext):
        self.search_for_instance = False

    # Entering identifier rule
    def enterIdentifier(self, ctx:VhdlParser.IdentifierContext):
        if ((self.search_for_instance and
            # easy way to get rid of noise
            ctx.BASIC_IDENTIFIER().__str__() != "work" and
            ctx.BASIC_IDENTIFIER().__str__() != "rtl") or
            self.search_for_port_map or
            self.in_signal_assignment):
            print(ctx.BASIC_IDENTIFIER())

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



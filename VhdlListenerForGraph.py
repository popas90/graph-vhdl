from antlr4 import *
from VhdlListener import VhdlListener
from VhdlParser import VhdlParser

# This class defines a complete listener for a parse tree produced by VhdlParser.
class VhdlListenerForGraph(VhdlListener):

    def __init__(self):
        self.search_for_instance = False

    # Entering the instantiation_unit rule
    def enterInstantiated_unit(self, ctx:VhdlParser.Instantiated_unitContext):
        self.search_for_instance = True

    # Exiting the instantiation_unit rule
    def exitInstantiated_unit(self, ctx:VhdlParser.Instantiated_unitContext):
        self.search_for_instance = False

    # Entering identifier rule
    def enterIdentifier(self, ctx:VhdlParser.IdentifierContext):
        if (self.search_for_instance and
            # easy way to get rid of noise
            ctx.BASIC_IDENTIFIER().__str__() != "work" and
            ctx.BASIC_IDENTIFIER().__str__() != "rtl"):
            print(ctx.BASIC_IDENTIFIER())
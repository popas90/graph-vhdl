from VhdlVisitor import VhdlVisitor
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .VhdlParser import VhdlParser
else:
    from VhdlParser import VhdlParser
from VhdlParser import VhdlParser

class VhdlVisitorForGraph(ParseTreeVisitor):

    # Visit a parse tree produced by VhdlParser#identifier.
    def visitIdentifier(self, ctx:VhdlParser.IdentifierContext):
        if (ctx.BASIC_IDENTIFIER()):
            print(ctx.BASIC_IDENTIFIER())

        if (ctx.EXTENDED_IDENTIFIER()):
            print(ctx.EXTENDED_IDENTIFIER())
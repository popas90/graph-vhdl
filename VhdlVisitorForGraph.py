from VhdlVisitor import VhdlVisitor
from VhdlParser import VhdlParser

class VhdlVisitorForGraph(VhdlVisitor):

    # Visit a parse tree produced by VhdlParser#identifier.
    def visitIdentifier(self, ctx:VhdlParser.IdentifierContext):
        print(ctx.BASIC_IDENTIFIER())
        print(ctx.EXTENDED_IDENTIFIER())
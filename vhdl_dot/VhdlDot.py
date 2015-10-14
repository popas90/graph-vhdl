from graphviz import Digraph
from abc import ABCMeta


class VhdlDot(metaclass=ABCMeta):

    _dot = None

    def __init__(self):
        """
        Creates a Digraph reference shared by all instances
        :type self: VhdlDotBaseClass
        """
        if self.__class__._dot is None:
            self.__class__._dot = Digraph(name="top_level", format  ="png")

    def get_dot(self):
        """
        Returns a reference to the main digraph
        :rtype: Digraph
        :return: digraph reference
        """
        return self.__class__._dot

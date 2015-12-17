from graphviz import Digraph


class DotBase:

    instance = None

    def __init__(self):
        """
        Creates a Digraph reference shared by all instances
        :type self: VhdlDotBaseClass
        """
        if not DotBase.instance:
            DotBase.instance = Digraph(name="top_level", format="pdf")

    def add_node(self):
        pass

    def add_edge(self):
        pass

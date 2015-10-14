from VhdlDot import VhdlDot


class ComponentDot(VhdlDot):

    """
    Adds a DOT node representing a VHDL component. Currently, supports only
    input/output ports (as lists) and a component name.
    """
    def __init__(self, name, input_ports, output_ports):
        super.__init__()

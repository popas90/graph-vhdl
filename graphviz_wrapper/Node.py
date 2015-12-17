import DotBase
import itertools


class Node(DotBase):

    def __init__(self, name, inputs, outputs):
        dot = DotBase()
        # TODO make this a class method
        dot.get_dot().node(name,
                           self._build_node_structure(name, inputs, outputs))
        print(dot.get_dot().source)
        dot.get_dot().render('output/round-table.gv', view=True)

    def _build_node_structure(self, name, inputs, outputs):
        node_structure = \
            '<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">\n'
        add_name = True
        for inp, outp in itertools.zip_longest(inputs, outputs):
            print(inp, outp)
            node_structure += '<TR>\n'
            inp = inp if inp is not None else " "
            outp = outp if outp is not None else " "
            comp_name = name if add_name is True else " "
            add_name = False
            node_structure += '<TD PORT="{0}">{0}</TD>\n'.format(inp)
            node_structure += '<TD>{0}</TD>\n'.format(comp_name)
            node_structure += '<TD PORT="{0}">{0}</TD>\n'.format(outp)
            node_structure += '</TR>\n'
        node_structure += '</TABLE>>'
        return node_structure


if __name__ == '__main__':
    node = Node('main_node', ['first_in', 'second_in'], ['first_out'])

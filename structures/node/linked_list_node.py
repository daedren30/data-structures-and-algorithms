from structures.node.basic_node import BasicNode

class LinkedListNode(BasicNode):
    """A node for linked lists inheriting from BasicNode
    Attributes: data, next, prev
    Overrides: __str__, __repr__, __eq__, __ne__, __lt__, __gt__
    Getters: get_data, get_next
    Setters: set_data, set_next
    """
    def __init__(self, data):
        super().__init__(data)
        self.prev = None

    # set previous node
    def set_prev(self, prev):
        self.prev = prev
        
    # get previous node
    def get_prev(self):
        return self.prev
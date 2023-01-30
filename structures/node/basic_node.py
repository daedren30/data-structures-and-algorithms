class BasicNode:
    """A basic node
    Attributes: data, next
    Overrides: __str__, __repr__, __eq__, __ne__, __lt__, __gt__
    Getters: get_data, get_next
    Setters: set_data, set_next
    """
    def __init__(self, data):
        self.data = data
        self.next = None

    # override the default string representation of the object
    def __str__(self):
        return str(self.data)

    # override the default string representation of the object
    def __repr__(self):
        return str(self.data)

    # override the default equality operator
    def __eq__(self, other):
        return self.data == other.data
    
    # override the default inequality operator
    def __ne__(self, other):
        return self.data != other.data
    
    # override the default less than operator
    def __lt__(self, other):
        return self.data < other.data
    
    # override the default greater than operator
    def __gt__(self, other):
        return self.data > other.data
    
    # get node data
    def get_data(self):
        return self.data
    
    # set node data
    def set_data(self, data):
        self.data = data

    # get next node
    def get_next(self):
        return self.next
    
    # set next node
    def set_next(self, next):
        self.next = next
        
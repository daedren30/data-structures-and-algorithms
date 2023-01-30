from structures.node.linked_list_node import LinkedListNode

class LinkedList:
    """Linked list using LinkedListNode
    Attributes: head, tail, size
    Overrides: __str__, __repr__, __eq__, __ne__, __lt__, __gt__
    Getters: get_head, get_tail, get_size
    Setters: set_head, set_tail, set_size
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    # override the default string representation of the object
    def __str__(self):
        while self.head != None:
            print(self.head)
            self.head = self.head.get_next()
            
    # override the default string representation of the object
    def __repr__(self):
        while self.head != None:
            print(self.head)
            self.head = self.head.get_next()
            
    # override the default equality operator
    def __eq__(self, other):
        while self.head != None:
            if self.head != other.head:
                return False
            self.head = self.head.get_next()
            other.head = other.head.get_next()
        return True

    # override the default inequality operator
    def __ne__(self, other):
        while self.head != None:
            if self.head != other.head:
                return True
            self.head = self.head.get_next()
            other.head = other.head.get_next()
        return False
    
    # override the default less than operator
    def __lt__(self, other):
        return self.size < other.size
    
    # override the default greater than operator
    def __gt__(self, other):
        return self.size > other.size
    
    # get the head of the list
    def get_head(self):
        return self.head
    
    # set the head of the list
    def set_head(self, head):
        self.head = head
    
    # get the tail of the list
    def get_tail(self):
        return self.tail
    
    # set the tail of the list
    def set_tail(self, tail):
        self.tail = tail
        
    # get the size of the list
    def get_size(self):
        return self.size
    
    # set the size of the list
    def set_size(self, size):
        self.size = size
        
    # add a node to the list
    def add(self, data):
        node = LinkedListNode(data)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.set_next(node)
            node.set_prev(self.tail)
            self.tail = node
        self.size += 1
        
    # remove a node from the list
    def remove(self, data):
        node = self.head
        while node != None:
            if node.get_data() == data:
                if node.get_prev() != None:
                    node.get_prev().set_next(node.get_next())
                else:
                    self.head = node.get_next()
                if node.get_next() != None:
                    node.get_next().set_prev(node.get_prev())
                else:
                    self.tail = node.get_prev()
                self.size -= 1
                return True
            node = node.get_next()
        return False
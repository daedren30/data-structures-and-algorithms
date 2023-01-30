# various tests for linked list

from structures.node.linked_list_node import LinkedListNode
from structures.linked_list.linked_list import LinkedList

def test_linked_list_node():
    node = LinkedListNode(1)
    assert node.get_data() == 1
    assert node.get_next() == None
    assert node.get_prev() == None
    node.set_data(2)
    assert node.get_data() == 2
    node.set_next(3)
    assert node.get_next() == 3
    node.set_prev(4)
    assert node.get_prev() == 4
    
def test_linked_list():
    """Test all methods of the linked list"""
    linked_list = LinkedList()
    assert linked_list.get_head() == None
    assert linked_list.get_tail() == None
    assert linked_list.get_size() == 0
    linked_list.add(1)
    assert linked_list.get_head().get_data() == 1
    assert linked_list.get_tail().get_data() == 1
    assert linked_list.get_size() == 1
    linked_list.add(2)
    assert linked_list.get_head().get_data() == 1
    assert linked_list.get_tail().get_data() == 2
    assert linked_list.get_size() == 2
    linked_list.add(3)
    assert linked_list.get_head().get_data() == 1
    assert linked_list.get_tail().get_data() == 3
    assert linked_list.get_size() == 3
    linked_list.remove(2)
    assert linked_list.get_head().get_data() == 1
    assert linked_list.get_tail().get_data() == 3
    assert linked_list.get_size() == 2
    linked_list.remove(1)
    assert linked_list.get_head().get_data() == 3
    assert linked_list.get_tail().get_data() == 3
    assert linked_list.get_size() == 1
    linked_list.remove(3)
    assert linked_list.get_head() == None
    assert linked_list.get_tail() == None
    assert linked_list.get_size() == 0
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)
    linked_list.add(4)
    linked_list.add(5)
    assert linked_list.get_head().get_data() == 1
    assert linked_list.get_tail().get_data() == 5
    assert linked_list.get_size() == 5
    linked_list.remove(3)
    assert linked_list.get_head().get_data() == 1
    assert linked_list.get_tail().get_data() == 5
    assert linked_list.get_size() == 4
    linked_list.remove(1)
    assert linked_list.get_head().get_data() == 2
    assert linked_list.get_tail().get_data() == 5
    assert linked_list.get_size() == 3
    linked_list.remove(5)
    assert linked_list.get_head().get_data() == 2
    assert linked_list.get_tail().get_data() == 4
    assert linked_list.get_size() == 2
    
if __name__ == "__main__":
    test_linked_list_node()
    test_linked_list()
    print("All tests passed successfully!")
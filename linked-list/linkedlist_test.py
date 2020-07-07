import unittest
from linkedlist import *

class NodeTest(unittest.TestCase):
    
    """
    Test initializing a Node.
    """
    def test_init(self):
        node = Node(1)
        assert node.data == 1
        assert node.next is None

class LinkedListTest(unittest.TestCase):

    """
    Test initializing a Linked List.
    """
    def test_init(self):
        ll = LinkedList()
        assert ll.head is None

    """
    Test is_empty() Method.
    """
    def test_is_empty(self):
        ll = LinkedList()
        assert ll.head is None

    """
    Test size() Method.
    """
    def test_size(self):
        return

    """
    Test prepend() Method.
    """
    def test_prepend(self):
        return

    """
    Test search() Method.
    """
    def test_search(self):
        return

    """
    Test insert() Method.
    """
    def test_insert(self):
        return

    """
    Test search() Method.
    """
    def test_remove(self):
        return
    
    """
    Test clear() Method.
    """
    def test_clear(self):
        return

    """
    Test any other methods you create!
    """
    
if __name__ == '__main__':
    unittest.main()

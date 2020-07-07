import unittest
from linkedlist import *

class NodeTest(unittest.TestCase):

    def test_init(self):
        '''Test initializing a Node.'''
        node = Node(1)
        assert node.data == 1
        assert node.next is None

class LinkedListTest(unittest.TestCase):

    def test_init(self):
        '''Test initializing a Linked List.'''
        ll = LinkedList()
        assert ll.head is None

    def test_is_empty(self):
        '''Test is_empty() Method.'''
        ll = LinkedList()
        assert ll.head is None

    def test_size(self):
        '''Test size() Method.'''
        return

    def test_prepend(self):
        '''Test prepend() Method.'''
        return

    def test_append(self):
        '''Test append() Method.'''
        return

    def test_search(self):
        '''Test search() Method.'''
        return

    def test_insert(self):
        '''Test insert() Method.'''
        return

    def test_remove(self):
        '''Test remove() Method.'''
        return
    
    def test_clear(self):
        '''Test clear() Method.'''
        return
    
    '''Test any other methods you create!'''
    
if __name__ == '__main__':
    unittest.main()

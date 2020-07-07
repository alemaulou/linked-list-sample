'''
A Linked List is a data structure compased by a chain of Node objects.
Each Node contains a value and a pointer to the next node in the chain.
Python does not ship a built-in Linked List data structure like Java.
It is your job to implement a Linked List class along with key operations.
'''

class Node:
    def __init__(self, data, next=None):
        """
        Initialize node with empty reference field.
        """
        self.data = data
        self.next = next

    def __repr__(self):
        """
        To print to console.
        """
        return self.data

    
class LinkedList:
    def __init__(self):
        """
        Create a linked list. Try to come up with solutions with a `head` reference first.
        Then try implementing a `tail` reference.
        Time Complexity: O(1) Constant Time
        """
        self.head = None
        # self.tail = None

    def __repr__(self):
        """
        Return a string representation of linked list.
        Time Complexity: O(n) Linear Time
        """
        nodes = []
        current = self.head
        while current:
            nodes.append(current.data)
            current = current.next
        return str(nodes)

    def is_empty(self):
        """
        Check if list is empty. 
        Time Complexity: O(1) Constant Time
        """
        return self.head is None

    def size(self):
        """
        Return the number of elements in the list.
        Time Complexity: O(n) Linear Time
        """

    def prepend(self, data):
        """
        Add node to the *beginning* of the list.
        Time Complexity: O(1)
        """

    def append(self, data):
        """
        Add node to the *end* of the LinkedList.
        Time Complexity: O(n) (without tail)
                         O(1) (with tail)
        """

    def search(self, value):
        """
        Search for the first node with data matching 'value'.
        Return element or None if element not found in Linked List.
        Time Complexity: O(n)
        """

    def insert(self, data):
        """
        Search for the first node with data matching 'value'.
        Return element or None if element not found in Linked List.
        Time Complexity: O(n)
        """

    def remove(self, value):
        """
        Remove first occurrence of node with data matching 'value'
        from the linked list. 
        Time Complexity: O(n) *Must *search* for node before deleting.
        """

    def clear(self):
        """
        Clear all nodes in the linked list.
        Time Complexity: O(1)
        """

'''
Challenges:
    1) Implement more LinkedList methods (see Java Linked List documentation here: https://docs.oracle.com/javase/7/docs/api/java/util/LinkedList.html)
    2) Implement a Stack class using the Linked List data structure you built.
    3) Top 20 Linked List Coding Interview Problems (https://www.geeksforgeeks.org/top-20-linked-list-interview-question/)
'''


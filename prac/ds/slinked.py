class Node:
    '''Node class used in singly linked list'''
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class SLinkedList:
    def __init__(self, head=None):
        self.head = head

    def add_head(self, data):
        '''Adds node with data to beginning of linked list'''
        self.head = Node(data, self.head)

    def add_last(self, data):
        '''Adds node with data to end of linked list'''
        if self.head is None:
            self.head = Node(data, None)
            return
        current = self.head
        while current.next_node is not None:
            current = current.next_node
        current.next_node = Node(data, None)

    def combine(self, other):
        '''Combines 2 singly linked lists'''
        self.add_last(other.head)

    def remove_head(self):
        '''Removes first node if not empty'''
        if self.head is None:
            raise Exception("Cannot remove head from empty list")
        self.head = self.head.next_node

    def remove(self, data):
        '''Removes first node with matching data, if contained'''
        current = self.first
        while current is not None:
            if current.data == data:
                if current.next_node is None:
                    self.remove_last()
                elif current.prev_node is None:
                    self.remove_first()
                else:
                    current.prev_node.next_node = current.next_node
                    current.next_node.prev_node = current.prev_node
                return
                self.size -= 1
            current = current.next_node
        raise ValueError("Data must be contained in list")

    def index_of(self, data):
        '''
            Returns index of data if contained in list.
            Checks for cycle while calculating index
        '''
        if self.head is None:
            return False
        fast = self.head.next_node
        slow = self.head
        index = 0
        meets = 0
        while fast is not None and fast.next_node is not None:
            if fast == slow:
                meets += 1
                if meets > 2:       # Occurs if data not in list and list is cycle
                    raise ValueError("data must be contained in list")

            if slow.data == data:
                return index

            fast = fast.next_node.next_node
            slow = slow.next_node
            index += 1

        while slow is not None:
            if slow.data == data:
                return index
            slow = slow.next_node
            index += 1

        raise ValueError("data must be contained in list")

    def each(self):
        '''Yields data of each element of linked list'''
        if self.head is None:
            return None
        current = self.head
        while current.next_node is not None:
            yield current.data
            current = current.next_node

    def has_cycle(self) -> bool:
        '''Check if single linked list starting at start has a cycle'''
        if self.head is None:
            return False
        fast = self.head.next_node
        slow = self.head
        while fast is not None and fast.next_node is not None:
            if fast == slow:
                return True
            fast = fast.next_node.next_node
            slow = slow.next_node
        return False

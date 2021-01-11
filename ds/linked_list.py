class Node:
    '''Node class used in doubly linked list'''
    def __init__(self, value, prev_node, next_node):
        self.value = value
        self.prev_node = prev_node
        self.next_node = next_node


class DLinkedList:
    '''Doubly Linked List Class'''
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def size(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return self.size == 0

    def add(self, value):
        self.add_last(value)

    def add_first(self, value):
        if self.is_empty():
            self.first = Node(value, None, None)
            self.last = self.first
        else:
            self.first = Node(value, None, self.first)
        self.size += 1

    def add_last(self, value):
        if self.is_empty():
            self.first = Node(value, None, None)
            self.last = self.first
        else:
            self.last.next_node = Node(value, self.last, None)
            self.last = self.last.next_node
        self.size += 1

    def insert_at(self, value, index: int):
        '''Inserts such that a node containing value will lie at index'''
        if 0 > index > self.size:
            raise ValueError("Index must be less than list size")

        if index == 0:
            self.add_first(value)

        elif index == self.size:
            self.add_last(value)

        # Search from beggining of linked list
        elif index < self.size / 2:
            current = self.first
            for _ in range(index - 1):
                current = current.next_node
            current.next_node.prev_node = Node(value,
                                               current.prev_node,
                                               current.next_node)
            current.next_node = current.next_node.prev_node

        # Search from end of linked list
        else:
            current = self.last
            for _ in range(self.size - index + 2):
                current = current.prev_node
            current.prev_node.next_node = Node(value,
                                               current.prev_node,
                                               current.next_node)
            current.prev_node = current.prev_node.next_node
        self.size += 1

    def add_list(self, other):
        '''Appends DLinkedList, other, to self'''
        if not isinstance(other, DLinkedList):
            raise TypeError("Must add DLinkedList to DLinkedList")
        self.last.next_node = other.first
        self.last = other.last
        self.size += other.size

    def remove(self, value):
        '''Removes node with value from list, if contained'''
        current = self.first
        while current is not None:
            if current.value == value:
                if current.next_node is None:
                    self.remove_last()
                elif current.prev_node is None:
                    self.remove_first()
                else:
                    current.prev_node.next_node = current.next_node
                    current.next_node.prev_node = current.prev_node
                return
            current = current.next_node
        raise ValueError("Value must be contained in list")
        self.size -= 1

    def remove_first(self):
        if self.first is None:
            raise Exception("Cannot remove first = None")
        self.first = self.first.next_node
        self.first.prev_node = None
        self.size -= 1

    def remove_last(self):
        if self.last is None:
            raise Exception("Cannot remove last = None")
        self.last = self.last.prev_node
        self.last.next_node = None
        self.size -= 1

    def remove_at(self, index: int):
        if 0 > index >= self.size:
            raise ValueError("Index must be > 0 and < list size")

        # Search from beginning of linked list
        if index < self.size / 2:
            current = self.first
            for _ in range(index):
                current = current.next_node
            current.prev_node.next_node = current.next_node
            current.next_node.prev_node = current.prev_node

        # Search from end of linked list
        else:
            current = self.last
            for _ in range(self.size - index + 1):
                current = current.prev_node
            current.prev_node.next_node = current.next_node
            current.next_node.prev_node = current.prev_node
        self.size -= 1

    def index_of(self, value) -> int:
        current = self.first
        index = 0
        while current is not None:
            if current.value == value:
                return index
            current = current.next_node
            index += 1
        raise ValueError("Value must be contained in list")

    def __str__(self):
        current = self.first
        output = "[ "
        while current is not None:
            output += str(current.value) + " "
            current = current.next_node
        output += "]"
        return output

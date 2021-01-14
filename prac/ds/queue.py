from dlinked import Node


class Queue:
    '''Queue implementation using doubly linked list'''
    def __init__(self):
        self.last = None
        self.first = None
        self.size = 0

    def size(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return (self.size == 0)

    def enqueue(self, value):
        if self.is_empty():
            self.first = Node(value, None, None)
            self.last = self.first
        else:
            self.last.next_node = Node(value, None, self.last)
            self.last = self.last.prev_node

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue empty")
        else:
            temp = self.first
            self.first = self.first.prev_node
            return temp

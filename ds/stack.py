class Stack:
    def __init__(self, values: list):
        self.values = values

    def __repr__(self):
        return ' '.join([str(value) for value in self.values])

    def size(self) -> int:
        return len(self.values)

    def is_empty(self):
        return (len(self.values) == 0)

    def push(self, value):
        self.values.append(value)

    def pop(self):
        if self.is_empty():
            raise Exception('Cannot pop value from an empty stack')
        return self.values.pop()

    def top_value(self):
        if len(self.values) == 0:
            return float('inf')
        return self.values[-1]

class HeapBinaryMin:
    def __init__(self, data=[]):
        self.data = data
        self.build_max_heap()

    def build_min_heap(self):
        pass

    def get_min(self):
        return self.data[0]

    def extract_min(self):
        popped, self.data[0] = self.data[0], self.data[-1]
        
        return popped

    def insert(self, A: list):
        current = len(self.data)
        self.data.append(A)

        while self.data[current] < self.data[self.parent(current)]:
            self.data[current], self.data[self.parent(current)] = self.data[self.parent(current)], self.data[current]
            current = self.parent(current)

    def min_heapify(self, index):
        pass

    def parent(self, index: int) -> int:
        '''Returns position of parent of element at index'''
        return index // 2

    def left_child(self, index: int) -> int:
        '''Returns position of left child of element at index'''
        return 2 * index

    def right_child(self, index):
        '''Returns position of right child of element at index'''
        return 2 * index + 1

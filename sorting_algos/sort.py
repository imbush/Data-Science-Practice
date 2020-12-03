import numpy
def selection_sort(arr: list):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)): # loops through items after i
            if arr[j] < arr[i]: #switches if lower than arr[i]
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def bubble_sort(arr: list):
    sort_made = True
    while sort_made:
        sort_made = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sort_made = True
    return arr

def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        while arr[i-1] > arr[i] and i != 0: # pushes item back until it is greater than the next item
            arr[i], arr[i-1] = arr[i-1], arr[i] #swaps if less than previous item
            i -= 1
    return arr

def merge(arr1: list, arr2: list):
    '''merges two sorted ascending lists'''
    arr3 =[]
    while arr1 and arr2: #while not empty
        if arr1[0] < arr2[0]:
            arr3.append(arr1.pop(0))
        else:
            arr3.append(arr2.pop(0))
    return arr3 + arr1 + arr2 #adds remaining items in arr1 or arr2

def merge_sort(arr: list):
    '''bottum up'''
    arr = [[x] for x in arr] #turns arr into a list of 1 element lists
    while len(arr) != 1:
        arr = [merge(arr[2*x], arr[2*x+1]) for x in range(len(arr)//2)]+ arr[2*(len(arr)//2):]# merges pairs of elements in arr, adds last element if odd length
    return arr[0]

def lomuto_partition(arr: list, low: int, high: int):
    pivot = arr[high]
    i = low
    for j in range(low, high+1):
        if arr[j] < pivot:
            arr[i],arr[j] = arr[j],arr[i]
            i += 1
    arr[i],arr[high] = arr[high], arr[i]
    return arr, i

def hoare_partition(arr: list, low: int, high: int):
    pivot = arr[(low+high)//2]
    i = low
    j = high
    while True:
        while arr[i] < pivot:#increments i and j until they are 
            i += 1
            
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return arr, j
        arr[i],arr[j] = arr[j],arr[i]
        i += 1
        j -= 1

def quick_sort(arr: list, low: int, high: int):
    if low < high:
        arr, pivot = hoare_partition(arr, low, high) #switch lomuto, hoare here
        arr = quick_sort(arr,low, pivot)
        arr = quick_sort(arr, pivot+1, high)
    return arr

class Node:
    def __init__(self, key, lchild = None, rchild = None):
        self.key = key
        self.lchild = lchild
        self.rchild = rchild

    def insert(self, new: int):
        '''Inserts value in bst starting at self'''
        if new < self.key:
            if self.lchild == None:
                self.lchild = Node(new)
            else:
                self.lchild.insert(new)
            
        else:
            if self.rchild == None:
                self.rchild = Node(new)
            else:
                self.rchild.insert(new)

def return_sorted(node, arr):
    if node == None:
        return arr
    arr = return_sorted(node.lchild, arr)
    arr.append(node.key) #nodes' key nested between those to the left(<) and to the right (>)
    arr = return_sorted(node.rchild, arr)
    return arr

def tree_sort(arr: list):
    root = Node(arr[0])
    for i in arr[1:]:
        root.insert(i)
    return return_sorted(root, [])

if __name__ == "__main__":
    arr = [3,1,4,1,5,9,2,6,5,3,13]
    #print(merge_sort(arr))
    #print(quick_sort(arr, 0, len(arr)-1))
    print(bubble_sort(arr))
class Node:
    def __init__(self, val=None):
        self.children = dict()  # Map from character to node
        self.val = val


class Trie:
    def __init__(self):
        self.root = Node()

    def find(self, key: str):
        """Return val of node with key."""
        current = self.root
        for char in key:
            if char in current.children:
                current = current.children[char]
            else:
                return None
        return current.val

    def insert(self, key: str, val) -> None:
        """Insert or rewrite node with val at key."""
        current = self.root
        for char in key:
            if char not in current.children:
                current.children[char] = Node()
            current = current.children[char]
        current.val = val

    def delete_node(self, key: str) -> None:
        """Delete value of node at key."""
        current = self.root
        for char in key:
            if char not in current.children:
                return None
            current = current.children[char]
        current.val = None

    def delete_branch(self, key: str, node=None, d=0) -> bool:
        """Delete value of node at key, node, and all unnecessarry parent nodes."""
        if node is None:
            node = self.root

        if d == len(key):
            node.val = None
        else:
            char = key[d]
            if char in node.children and self.delete_branch():
                del node.children[char]
        return node.val is None and len(node)

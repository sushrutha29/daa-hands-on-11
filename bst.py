class TreeNode:
    def __init__(self, val):
        self.val = val
        self.leftnode = None
        self.rightnode = None

class BinarySearchTree:
    def __init__(self):
        self.rootnode = None

    def insert(self, val):
        if not self.rootnode:
            self.rootnode = TreeNode(val)
        else:
            self.insertrecursive(self.rootnode, val)

    def insertrecursive(self, Node, val):
        if val < Node.val:
            if Node.leftnode:
                self.insertrecursive(Node.leftnode, val)
            else:
                Node.leftnode = TreeNode(val)
        elif val > Node.val:
            if Node.rightnode:
                self.insertrecursive(Node.rightnode, val)
            else:
                Node.rightnode = TreeNode(val)

    def search(self, val):
        return self.searchrecursive(self.rootnode, val)

    def searchrecursive(self, Node, val):
        if not Node:
            return False
        elif Node.val == val:
            return True
        elif val < Node.val:
            return self.searchrecursive(Node.leftnode, val)
        else:
            return self.searchrecursive(Node.rightnode, val)

    def delete(self, val):
        self.rootnode = self.deleterecursive(self.rootnode, val)

    def deleterecursive(self, Node, val):
        if not Node:
            return Node

        if val < Node.val:
            Node.leftnode = self.deleterecursive(Node.leftnode, val)
        elif val > Node.val:
            Node.rightnode = self.deleterecursive(Node.rightnode, val)
        else:
            if not Node.leftnode:
                return Node.rightnode
            elif not Node.rightnode:
                return Node.leftnode

            Node.val = self._min_value_Node(Node.rightnode).val

            Node.rightnode = self.deleterecursive(Node.rightnode, Node.val)

        return Node

    def _min_value_Node(self, Node):
        current = Node
        while current.leftnode:
            current = current.leftnode
        return current

def test_binary_search_tree():
    bst = BinarySearchTree()
    bst.insert(6)
    bst.insert(5)
    bst.insert(8)
    bst.insert(9)
    bst.insert(3)
    bst.insert(2)
    bst.insert(1)

    assert bst.search(2) == True
    assert bst.search(5) == True
    assert bst.search(6) == True
    assert bst.search(13) == False

    bst.delete(1)
    assert bst.search(1) == False
    assert bst.search(2) == True

    print("All tests cases passed")

if __name__ == "__main__":
    test_binary_search_tree()

"""
output:
All tests cases passed
"""

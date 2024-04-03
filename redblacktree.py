class Node:
    def __init__(self, key, color='RED'):
        self.key = key
        self.leftnode = None
        self.rightnode = None
        self.parentnode = None
        self.color = color

class RedBlackTree:
    def __init__(self):
        self.nil = Node(None, color='BLACK')
        self.rootnode = self.nil

    def insert(self, key):
        new_node = Node(key)
        new_node.leftnode = self.nil
        new_node.rightnode = self.nil

        parentnode = None
        currentnode = self.rootnode

        while currentnode != self.nil:
            parentnode = currentnode
            if new_node.key < currentnode.key:
                currentnode = currentnode.leftnode
            else:
                currentnode = currentnode.rightnode

        new_node.parentnode = parentnode

        if parentnode == None:
            self.rootnode = new_node
        elif new_node.key < parentnode.key:
            parentnode.leftnode = new_node
        else:
            parentnode.rightnode = new_node

        new_node.color = 'RED'
        self.balanceInsertion(new_node)

    def balanceInsertion(self, node):
        while node.parentnode and node.parentnode.color == 'RED':
            if node.parentnode == node.parentnode.parentnode.leftnode:
                uncle = node.parentnode.parentnode.rightnode
                if uncle.color == 'RED':
                    node.parentnode.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parentnode.parentnode.color = 'RED'
                    node = node.parentnode.parentnode
                else:
                    if node == node.parentnode.rightnode:
                        node = node.parentnode
                        self.left_rotation(node)
                    node.parentnode.color = 'BLACK'
                    node.parentnode.parentnode.color = 'RED'
                    self.right_rotation(node.parentnode.parentnode)
            else:
                uncle = node.parentnode.parentnode.leftnode
                if uncle.color == 'RED':
                    node.parentnode.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parentnode.parentnode.color = 'RED'
                    node = node.parentnode.parentnode
                else:
                    if node == node.parentnode.left:
                        node = node.parentnode
                        self.rightnode_rotate(node)
                    node.parentnode.color = 'BLACK'
                    node.parentnode.parentnode.color = 'RED'
                    self.left_rotation(node.parentnode.parentnode)
        self.rootnode.color = 'BLACK'

    def left_rotation(self, x):
        y = x.rightnode
        x.rightnode = y.leftnode
        if y.leftnode != self.nil:
            y.leftnode.parentnode = x
        y.parentnode = x.parentnode
        if x.parentnode == None:
            self.rootnode = y
        elif x == x.parentnode.leftnode:
            x.parentnode.leftnode = y
        else:
            x.parentnode.rightnode = y
        y.leftnode = x
        x.parentnode = y

    def right_rotation(self, y):
        x = y.leftnode
        y.leftnode = x.rightnode
        if x.rightnode != self.nil:
            x.rightnode.parentnode = y
        x.parentnode = y.parentnode
        if y.parentnode == None:
            self.rootnode = x
        elif y == y.parentnode.leftnode:
            y.parentnode.leftnode = x
        else:
            y.parentnode.rightnode = x
        x.rightnode = y
        y.parentnode = x

    def search(self, key):
        return self._search(self.rootnode, key)

    def _search(self, node, key):
        if node == self.nil or key == node.key:
            return node
        if key < node.key:
            return self._search(node.leftnode, key)
        else:
            return self._search(node.rightnode, key)

    def replace(self, u, v):
        if u.parentnode == None:
            self.rootnode = v
        elif u == u.parentnode.leftnode:
            u.parentnode.leftnode = v
        else:
            u.parentnode.rightnode = v
        v.parentnode = u.parentnode

    def delete(self, key):
        z = self.search(key)
        if z == self.nil:
            return
        y = z
        y_original_color = y.color
        if z.leftnode == self.nil:
            x = z.rightnode
            self.replace(z, z.rightnode)
        elif z.rightnode == self.nil:
            x = z.leftnode
            self.replace(z, z.leftnode)
        else:
            y = self.minimum(z.rightnode)
            y_original_color = y.color
            x = y.rightnode
            if y.parentnode == z:
                x.parentnode = y
            else:
                self.replace(y, y.rightnode)
                y.rightnode = z.rightnode
                y.rightnode.parentnode = y
            self.replace(z, y)
            y.leftnode = z.leftnode
            y.leftnode.parentnode = y
            y.color = z.color
        if y_original_color == 'BLACK':
            self.balancedeletion(x)

    def balancedeletion(self, x):
        while x != self.rootnode and x.color == 'BLACK':
            if x == x.parentnode.leftnode:
                w = x.parentnode.rightnode
                if w.color == 'RED':
                    w.color = 'BLACK'
                    x.parentnode.color = 'RED'
                    self.left_rotation(x.parentnode)
                    w = x.parentnode.rightnode
                if w.leftnode.color == 'BLACK' and w.rightnode.color == 'BLACK':
                    w.color = 'RED'
                    x = x.parentnode
                else:
                    if w.rightnode.color == 'BLACK':
                        w.leftnode.color = 'BLACK'
                        w.color = 'RED'
                        self.right_rotation(w)
                        w = x.parentnode.rightnode
                    w.color = x.parentnode.color
                    x.parentnode.color = 'BLACK'
                    w.rightnode.color = 'BLACK'
                    self.left_rotate(x.parentnode)
                    x = self.rootnode
            else:
                w = x.parentnode.leftnode
                if w.color == 'RED':
                    w.color = 'BLACK'
                    x.parentnode.color = 'RED'
                    self.right_rotate(x.parentnode)
                    w = x.parentnode.leftnode
                if w.rightnode.color == 'BLACK' and w.leftnode.color == 'BLACK':
                    w.color = 'RED'
                    x = x.parentnode
                else:
                    if w.leftnode.color == 'BLACK':
                        w.rightnode.color = 'BLACK'
                        w.color = 'RED'
                        self.left_rotate(w)
                        w = x.parentnode.leftnode
                    w.color = x.parentnode.color
                    x.parentnode.color = 'BLACK'
                    w.leftnode.color = 'BLACK'
                    self.right_rotate(x.parentnode)
                    x = self.rootnode
        x.color = 'BLACK'

    def minimum(self, node):
        while node.leftnode != self.nil:
            node = node.leftnode
        return node

# Test cases
def test_red_black_tree():
    r = RedBlackTree()
    r.insert(21)
    r.insert(4)
    r.insert(9)
    r.insert(11)
    r.insert(5)
    r.insert(18)
    r.insert(3)
    r.insert(31)
    r.insert(19)

    assert r.search(11).key == 11
    assert r.search(19).key == 19
    assert r.search(3).key == 3
    assert r.search(1) == r.nil

    r.delete(31)
    assert r.search(31) == r.nil
    
    
    print("All tests cases passed")

if __name__ == "__main__":
    test_red_black_tree()

"""
output:
All tests cases passed
"""


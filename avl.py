class AVLNode:
    def __init__(self, key):
        self.key = key
        self.leftnode = None
        self.rightnode = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.rootnode = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance(self, node):
        if not node:
            return 0
        return self.height(node.leftnode) - self.height(node.rightnode)

    def rightrotation(self, y):
        x = y.leftnode
        z = x.rightnode

        x.rightnode = y
        y.leftnode = z

        y.height = 1 + max(self.height(y.leftnode), self.height(y.rightnode))
        x.height = 1 + max(self.height(x.leftnode), self.height(x.rightnode))

        return x

    def leftrotation(self, x):
        y = x.rightnode
        z = y.leftnode

        y.leftnode = x
        x.rightnode = z

        x.height = 1 + max(self.height(x.leftnode), self.height(x.rightnode))
        y.height = 1 + max(self.height(y.leftnode), self.height(y.rightnode))

        return y

    def insert(self, node, key):
        if not node:
            return AVLNode(key)
        elif key < node.key:
            node.leftnode = self.insert(node.leftnode, key)
        else:
            node.rightnode = self.insert(node.rightnode, key)

        node.height = 1 + max(self.height(node.leftnode), self.height(node.rightnode))

        balance = self.balance(node)

        # Left Left Case
        if balance > 1 and key < node.leftnode.key:
            return self.rightrotation(node)

        # Right Right Case
        if balance < -1 and key > node.rightnode.key:
            return self.leftrotation(node)

        # Left Right Case
        if balance > 1 and key > node.leftnode.key:
            node.leftnode = self.leftrotation(node.leftnode)
            return self.rightrotation(node)

        # Right Left Case
        if balance < -1 and key < node.rightnode.key:
            node.rightnode = self.rightrotation(node.rightnode)
            return self.leftrotation(node)

        return node

    def delete(self, rootnode, key):
        if not rootnode:
            return rootnode

        if key < rootnode.key:
            root.leftnode = self.delete(rootnode.leftnode, key)
        elif key > rootnode.key:
            root.rightnode = self.delete(root.rightnode, key)
        else:
            if root.leftnode is None:
                temp = rootnode.rightnode
                rootnode = None
                return temp
            elif rootnode.rightnode is None:
                temp = rootnode.leftnode
                rootnode = None
                return temp

            temp = self.min_value_node(rootnode.rightnode)
            rootnode.key = temp.key
            rootnode.right = self.delete(rootnode.rightnode, temp.key)

        if rootnode is None:
            return rootnode

        rootnode.height = 1 + max(self.height(rootnode.leftnode), self.height(rootnode.rightnode))
        balance = self.balance(rootnode)

        if balance > 1 and self.balance(rootnode.leftnode) >= 0:
            return self.rightrotation(rootnode)

        if balance > 1 and self.balance(rootnode.leftnode) < 0:
            rootnode.leftnode = self.leftrotation(rootnode.leftnode)
            return self.rightrotation(rootnode)

        if balance < -1 and self.balance(rootnode.rightnode) <= 0:
            return self.leftrotation(rootnode)

        if balance < -1 and self.balance(rootnode.rightnode) > 0:
            rootnode.rightnode = self.rightrotation(rootnode.rightnode)
            return self.leftrotation(rootnode)

        return rootnode

    def min_value_node(self, node):
        current = node
        while current.leftnode is not None:
            current = current.leftnode
        return current

    def query(self, rootnode, key):
        if not rootnode:
            return False
        elif rootnode.key == key:
            return True
        elif key < rootnode.key:
            return self.query(rootnode.leftnode, key)
        else:
            return self.query(rootnode.rightnode, key)

    def inorder_traversal(self, rootnode):
        if rootnode:
            self.inorder_traversal(rootnode.leftnode)
            print(rootnode.key, end=" ")
            self.inorder_traversal(rootnode.rightnode)


if __name__ == "__main__":
    avl = AVLTree()
    keys = [13, 4, 9, 21, 54, 2, 15, 7, 5]
    for key in keys:
        avl.rootnode = avl.insert(avl.rootnode, key)

    print("Inorder Traversal AVL tree:")
    avl.inorder_traversal(avl.rootnode)
    print()

    search_keys = [21, 53]

    for key in search_keys:
        if avl.query(avl.rootnode, key):
            print(f"{key} is in AVL tree")
        else:
            print(f"{key} is not in AVL tree")

"""
output:
Inorder Traversal AVL tree:
2 4 5 7 9 13 15 21 54 
21 is in AVL tree
53 is not in AVL tree
"""

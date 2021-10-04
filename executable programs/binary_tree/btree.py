class BinaryNode:

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:

    def __init__(self, root):
        self.root = root

    def tree_traversal(self, root):
        if root:
            print(f"Preorder: {root.data}")
            self.tree_traversal(root.left)
            print(f"Inorder: {root.data}")
            self.tree_traversal(root.right)
            print(f"Postorder: {root.data}")


if __name__ == '__main__':
    left_node = BinaryNode(1)
    right_node = BinaryNode(3)
    root_node = BinaryNode(2, left_node, right_node)
    btree = BinaryTree(root_node)
    btree.tree_traversal(root_node)
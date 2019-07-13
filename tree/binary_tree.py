class BinaryNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insert_left(self, val):
        if not self.left:
            self.left = BinaryNode(val)
        else:
            tmp = BinaryNode(val)
            tmp.left = self.left
            self.left = tmp

    def insert_right(self, val):

        if not self.right:
            self.right = BinaryNode(val)
        else:
            tmp = BinaryNode(val)
            tmp.right = self.right
            self.right = tmp

    def get_right_child(self):
        return self.right

    def get_left_child(self):
        return self.left

    def _preorder_traversal(self, root):
        if not root:
            return
        print(root.val, end=' ')
        self._preorder_traversal(root.left)
        self._preorder_traversal(root.right)

    def preorder_traversal(self):
        self._preorder_traversal(self)
        print('\n')


if __name__ == '__main__':
    r = BinaryNode('a')
    r.insert_left('b')
    r.insert_right('c')
    r.preorder_traversal()
    r.insert_left('d')
    r.preorder_traversal()
    left = r.get_left_child()
    left.preorder_traversal()
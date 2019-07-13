class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def _insert(self, root, val):
        if not root:
            root = TreeNode(val)
        elif val < root.val:
            root.left = self._insert(root.left, val)
        elif val > root.val:
            root.right = self._insert(root.right, val)
        return root

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _print_tree(self, root):
        if not root:
            return
        self._print_tree(root.left)
        print(root.val, end=' ')
        self._print_tree(root.right)

    def print_tree(self):
        print('中序遍历结果: ', end='')
        self._print_tree(self.root)
        print('\r')

    def _query(self, root, val):
        if not root:
            return False
        if root.val == val:
            return True
        elif val < root.val:
            return self._query(root.left. val)
        elif val > root.val:
            return self._query(root.right, val)

    def query(self, val):
        return self._query(self.root, val)

    def _find_min(self, root):
        if root.left:
            return self._find_min(root.left)
        else:
            return root

    def find_min(self):
        return self._find_min(self.root).val

    def _find_max(self, root):
        if root.right:
            return self._find_max(root.right)
        else:
            return root

    def find_max(self):
        return self._find_max(self.root).val

    def _del_node(self, root, val):
        if not root:
            return
        if val < root.val:
            root.left = self._del_node(root.left, val)
        elif val > root.val:
            root.right = self._del_node(root.right, val)
        elif root.left and root.right:
            # 查找到要删除的节点，并且其左右节点都不为空
            # 找到右子树的最小节点代替要删除的节点，再删除最小节点
            tmp = self._find_min(root.right)
            root.val = tmp.val
            root.right = self._del_node(root.right, tmp.val)
        else:
            # 有一个节点为空
            root = root.left if root.left is not None else root.right
        return root

    def del_node(self, val):
        self._del_node(self.root, val)


if __name__ == '__main__':
    tree = BinarySearchTree()
    nums = [3, 1, 2, 4, 5]
    for num in nums:
        tree.insert(num)
    tree.print_tree()
    print('4 is in tree?', tree.query(4))
    print('min and max val of tree: ', tree.find_min(), tree.find_max())
    tree.del_node(2)
    print('删除节点2')
    tree.print_tree()
    tree.del_node(3)
    print('删除节点3')
    tree.print_tree()



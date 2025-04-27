# === inventory/avl_tree.py ===
class AVLNode:
    def __init__(self, key, value):
        self.key = key
        self.values = [value]
        self.left = self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if not node:
            return AVLNode(key, value)
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            node.values.append(value)
            return node

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return self._balance(node)

    def delete(self, key, value):
        self.root = self._delete(self.root, key, value)

    def _delete(self, node, key, value):
        if not node:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key, value)
        elif key > node.key:
            node.right = self._delete(node.right, key, value)
        else:
            if value in node.values:
                node.values.remove(value)
            if not node.values:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                min_larger_node = self._get_min(node.right)
                node.key, node.values = min_larger_node.key, min_larger_node.values
                node.right = self._delete(node.right, min_larger_node.key, min_larger_node.values[0])

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return self._balance(node)

    def _get_height(self, node):
        return node.height if node else 0

    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right)

    def _balance(self, node):
        balance = self._get_balance(node)
        if balance > 1:
            if self._get_balance(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1:
            if self._get_balance(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def _rotate_left(self, z):
        y = z.right
        z.right = y.left
        y.left = z
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _rotate_right(self, z):
        y = z.left
        z.left = y.right
        y.right = z
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _get_min(self, node):
        while node.left:
            node = node.left
        return node
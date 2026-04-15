class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def _insert(self, root, key) -> TreeNode:
        if not root:
            return TreeNode(key)
        if root.val < key:
            root.right = self._insert(root.right, key)
        elif root.val > key:
            root.left = self._insert(root.left, key)
        return root

    def _delete(self, root, key) -> TreeNode:
        if not root:
            return root

        if root.val < key:
            root.right = self._delete(root.right, key)
        elif root.val > key:
            root.left = self._delete(root.left, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            tmp = self._minValNode(root.right)
            root.val = tmp.val
            root.right = self._delete(root.right, tmp.val)
        return root
    
    def _minValNode(self, root):
        if not root:
            return None
        while root.left:
            root = root.left
        return root
    
    def _search(self, root, key):
        if not root:
            return False
        if key < root.val:
            return self._search(root.left, key)
        elif key > root.val:
            return self._search(root.right, key)
        return root.val == key
    
    def add(self, key):
        self.root = self._insert(self.root, key)
    
    def remove(self, key):
        self.root = self._delete(self.root, key)
    
    def contains(self, key):
        return self._search(self.root, key)


class MyHashSet:

    def __init__(self):
        self.size = 10000
        self.buckets = [BST() for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size
         
    def add(self, key: int) -> None:
        idx = self._hash(key)
        if not self.contains(key):
            self.buckets[idx].add(key)
        
    def remove(self, key: int) -> None:
        idx = self._hash(key)
        self.buckets[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx = self._hash(key)
        return self.buckets[idx].contains(key)
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
class MyHashSet:

    def __init__(self):
        self.sz = 1007
        self.st = [[] for _ in range(self.sz)]
        

    def hash(self, key):
        return key%1007

        

    def add(self, key: int) -> None:
        hk = self.hash(key)
        if not self.contains(key):
            self.st[hk].append(key)
        

    def remove(self, key: int) -> None:
        hk = self.hash(key)
        if self.contains(key):
            self.st[hk].remove(key)
        

    def contains(self, key: int) -> bool:
        hk = self.hash(key)
        for val in self.st[hk]:
            if val == key:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
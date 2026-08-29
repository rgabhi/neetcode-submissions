class FreqStack:

    def __init__(self):
        self.cnt = {}
        self.stacks = {}
        self.maxcnt = 0

    def push(self, val: int) -> None:
        self.cnt[val] = self.cnt.get(val, 0) + 1
        valcnt = self.cnt[val]
        if valcnt > self.maxcnt:
                self.maxcnt = valcnt
                self.stacks[valcnt] = []
        self.stacks[valcnt].append(val)

    def pop(self) -> int:
        val = self.stacks[self.maxcnt].pop()
        self.cnt[val] -= 1
        if not self.stacks[self.maxcnt]:
            self.maxcnt -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
class MinStack:

    def __init__(self):
        self.st = []
        self._min = float('inf')
        # [5, 4, 3, 6]
        # [0, -1, -1, 3]
        # 3
        # [5,4, 3, 6]
        # [0, 1, -1]
        # 0
    def push(self, val: int) -> None:
        if not self.st:
            self._min = val
        diff = val - self._min
        self.st.append(diff)
        if diff < 0:
            self._min = val

    def pop(self) -> None:
        diff = self.st.pop()
        if diff < 0:
            self._min = self._min - diff
        

    def top(self) -> int:
        if self.st:
            if self.st[-1] < 0:
                return self._min
            return self.st[-1] + self._min
        return -1
 

    def getMin(self) -> int:
        return self._min
        

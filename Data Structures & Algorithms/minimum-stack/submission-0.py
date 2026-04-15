class MinStack:

    def __init__(self):
        self.st = deque()
        self.min_st = deque()


    def push(self, val: int) -> None:
        self.st.append(val)
        if self.min_st:
            self.min_st.append(min(self.min_st[-1], val))
        else:
            self.min_st.append(val)

    def pop(self) -> None:
        if self.st: 
            self.st.pop()
            self.min_st.pop()
        

    def top(self) -> int:
        if self.st:
            return self.st[-1]
        return -1
        

    def getMin(self) -> int:
        if self.min_st:
            return self.min_st[-1]
        return -1

        

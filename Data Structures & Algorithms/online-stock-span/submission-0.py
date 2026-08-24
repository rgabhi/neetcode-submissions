class StockSpanner:

    def __init__(self):
        self.st = []

    def next(self, price: int) -> int:
        tmp = []
        span = 1
        while self.st and self.st[-1] <= price:
            tmp.append(self.st.pop())
            span += 1
        while tmp:
            self.st.append(tmp.pop())
        self.st.append(price)
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
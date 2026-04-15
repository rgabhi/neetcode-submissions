class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.last_idx = -1
        self.arr = [None]*capacity
        self.counter = 0


    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        if self.arr[i] is None:
            self.counter += 1
        self.arr[i] = n
        self.last_idx = max(i, self.last_idx)


    def pushback(self, n: int) -> None:
        if self.last_idx == (self.capacity-1):
            self.resize()
        self.last_idx += 1
        self.arr[self.last_idx] = n
        self.counter+=1


    def popback(self) -> int:
        pop_elem = self.arr[self.last_idx]
        self.arr[self.last_idx] = None
        self.last_idx -=1
        self.counter-=1
        return pop_elem

 

    def resize(self) -> None:
        self.arr = self.arr + [None]*self.capacity
        self.capacity *=2


    def getSize(self) -> int:
        return self.counter
        
        
    
    def getCapacity(self) -> int:
        return self.capacity

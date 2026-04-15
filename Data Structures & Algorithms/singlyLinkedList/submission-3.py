class LLNode:
    def __init__(self, val = -1, next = None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = LLNode()
        self.sz = 0

    
    def get(self, index: int) -> int:
        if index >= self.sz:
            return -1
        curr = self.head.next
        i = 0
        while i < index:
            curr = curr.next
            i += 1
        return curr.val 

    def insertHead(self, val: int) -> None:
        node = LLNode(val)
        tmp = self.head.next
        self.head.next = node
        node.next = tmp
        self.sz += 1

        

    def insertTail(self, val: int) -> None:
        curr = self.head.next
        if not curr:
            self.insertHead(val)
            return

        while curr.next:
            curr = curr.next
        newNode = LLNode(val)
        curr.next = newNode
        self.sz += 1

        

    def remove(self, index: int) -> bool:
        if index >= self.sz:
            return False
        i = 0
        prev = self.head
        curr = self.head.next
        while i < index:
            curr = curr.next
            prev = prev.next
            i += 1
        prev.next = curr.next
        del curr
        self.sz -= 1
        return True

        

    def getValues(self) -> List[int]:
        ans = []
        curr = self.head.next
        while curr:
            ans.append(curr.val)
            curr = curr.next
        return ans
        

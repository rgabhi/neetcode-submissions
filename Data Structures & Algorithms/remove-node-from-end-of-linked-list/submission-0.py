# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find length
        curr = head
        lenl = 0
        while curr:
            lenl += 1
            curr = curr.next
        # position to remove from beginning 
        pos = lenl - n + 1
        
        # if first position to remove
        if pos == 1:
            head = head.next
            return head
        
        cnt = 1
        curr = head
        while cnt < pos - 1:
            curr = curr.next
            cnt += 1
        # remove node
        curr.next = curr.next.next
        return head
            

        
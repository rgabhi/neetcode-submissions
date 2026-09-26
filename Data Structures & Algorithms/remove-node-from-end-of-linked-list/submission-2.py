# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return
        curr = head
        prev = None
        cnt = 0
        sz = 0
        while curr:
            sz += 1
            curr = curr.next
        curr = head
        n = sz - n
        if n == 0:
            return head.next
        while curr:
            if n == cnt:
                prev.next = curr.next
                break
            cnt += 1
            prev = curr
            curr = curr.next
        return head
        
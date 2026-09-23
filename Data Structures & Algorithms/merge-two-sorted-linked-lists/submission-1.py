# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        t = ListNode(-1)
        head = t
        while curr1 and curr2:
            if curr1.val < curr2.val:
                t.next = curr1
                t = t.next
                curr1 = curr1.next
            else:
                t.next = curr2
                t = t.next
                curr2 = curr2.next
        
        while curr1:
            t.next = curr1
            t = t.next
            curr1 = curr1.next

        while curr2:
            t.next = curr2
            t = t.next
            curr2 = curr2.next

        return head.next
        





        
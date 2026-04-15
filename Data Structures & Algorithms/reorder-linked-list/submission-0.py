# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        curr = head
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev
    
    def mergeLists(self, list1, list2):
        p1, p2 = list1, list2
        while p1 and p2:
            tmp1 = p1.next
            p1.next = p2
            tmp2 = p2.next
            p2.next = tmp1
            p1 = tmp1
            p2 = tmp2
        return list1

    def reorderList(self, head: Optional[ListNode]) -> None:
       # break list in two
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        list1 = head
        list2 = slow.next
        slow.next = None

        # reverse second list
        list2 = self.reverseList(list2)

        # merge lists
        head = self.mergeLists(list1, list2)
       


    
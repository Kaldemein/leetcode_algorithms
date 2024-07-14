from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        current = None

        carry = 0
        while l1 or l2 or carry:
            if l1: 
                l1_val = l1.val
            else :
                l1_val = 0
            
            if l2:
                l2_val = l2.val
            else:
                l2_val = 0
            
            total = l1_val + l2_val + carry
            carry = total // 10 

            if head == None:
                head = ListNode(total % 10)
                current = head
            else:
                current.next = ListNode(total %10)
                current = current.next

            if l1: 
                l1 = l1.next
            if l2: 
                l2 = l2.next 
        return head
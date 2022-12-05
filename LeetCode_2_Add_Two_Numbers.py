# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        p = dummy
        val, adv = 0, 0
        
        while l1 or l2 or adv:
            l1_val = 0
            if l1:
                l1_val = l1.val
                
            l2_val = 0
            if l2:
                l2_val = l2.val
                
            add = l1_val + l2_val + adv
            adv = add // 10
            val = add % 10
            p.next = ListNode(val)
            
            p = p.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next
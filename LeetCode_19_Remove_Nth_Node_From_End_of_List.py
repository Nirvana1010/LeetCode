# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # version -1
        num_nodes = 0
        tmp = head
        # get number of nodes
        while tmp:
            num_nodes += 1
            tmp = tmp.next
        
        index = 0
        tmp = head
        while True:
            index += 1
            # remove nth node from end
            if num_nodes == n:
                if num_nodes == 1:
                    return None
                else:
                    head = head.next
                    return head
            else:
                if index == num_nodes - n:
                    tmp.next = tmp.next.next
                    break
            tmp = tmp.next
        return head
        
        # version -2
        # dummy node
        dummy = ListNode(0, head)
        cur = dummy
        for i in range(1, num_nodes - n + 1):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next

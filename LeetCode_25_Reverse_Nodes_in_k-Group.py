class Solution:
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseList(head, tail):
            prev = tail.next
            curr = head
            while prev != tail:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return tail, head
        
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        
        while head:
            tail = prev
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            tail_next = tail.next
            head, tail = reverseList(head, tail)
            prev.next = head
            tail.next = tail_next
            head = tail.next
            prev = tail

        return dummy.next
        
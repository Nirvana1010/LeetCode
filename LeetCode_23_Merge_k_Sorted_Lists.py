# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(list1, list2):
            if not list1:
                return list2
            if not list2:
                return list1
            if list1.val <= list2.val:
                list1.next = mergeTwoLists(list1.next, list2)
                return list1
            else:
                list2.next = mergeTwoLists(list2.next, list1)
                return list2
        
        if not lists:
            return
        k = len(lists)
        step = 1
        while step < k:
            for i in range(0, k, step * 2):
                if i + step < k:
                    lists[i] = mergeTwoLists(lists[i], lists[i + step])
            step *= 2
        return lists[0]
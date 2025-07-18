# https://leetcode.com/problems/insertion-sort-list/
# https://youtu.be/Kk6mXAzqX3Y

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-5001)
        dummy.next = head
        pre = head
        cur = pre.next
        
        while cur:
            if pre.val <= cur.val:
                pre = cur
                cur = cur.next
                continue
                
            tmp = dummy
            while cur.val > tmp.next.val:
                tmp = tmp.next
            pre.next = cur.next
            cur.next = tmp.next
            tmp.next = cur
            cur = pre.next
        
        return dummy.next
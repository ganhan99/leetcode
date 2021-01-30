import collections
from typing import List
from collections import deque
# import math
from typing import List
import itertools

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:#感谢各位的更好思路或改进办法
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        thead = ListNode('a')
        thead.next = head
        pre,cur = None,thead
        while cur:
            pre=cur
            cur=cur.next
            while cur and cur.next and cur.next.val == cur.val:
                t=cur.val
                while cur and cur.val==t:
                    cur=cur.next
            pre.next=cur
        return thead.next


print(Solution().deleteDuplicates([1,2,3,3,4,4,5]))

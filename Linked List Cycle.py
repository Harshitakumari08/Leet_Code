class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head):
        if not head or not head.next:
            return False

        slow = head  # Slow pointer
        fast = head  # Fast pointer

        while fast and fast.next:
            slow = slow.next          
            fast = fast.next.next     

            if slow == fast:          
                return True
        return False  # No cycle found

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        # Move fast n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # Move both until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next

        # Remove nth node
        slow.next = slow.next.next

        return dummy.next
def build_list(values):
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)
    
head = build_list([1,2,3,4,5])
sol = Solution()
new_head = sol.removeNthFromEnd(head, 2)
print_list(new_head)   # Output: [1, 2, 3, 5]

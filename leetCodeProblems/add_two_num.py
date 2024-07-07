'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s = ListNode(0)
        ptr = s
        carry = 0
        while(l1 or l2 or carry):
            if(l1):
                carry += l1.val
                l1 = l1.next
            if(l2):
                carry += l2.val
                l2 = l2.next
            ptr.next = ListNode(carry % 10)
            ptr = ptr.next
            carry = carry // 10
        
        return s.next

# To test the code, you need to create ListNode objects
def create_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

# Test
l1 = create_linked_list([2,4,3])
l2 = create_linked_list([5,6,4])
sol = Solution()
result = sol.addTwoNumbers(l1, l2)

# Print result
while result:
    print(result.val, end=" ")
    result = result.next



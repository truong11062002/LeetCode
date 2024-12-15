# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        def add_with_carry(l1, l2, carry):
            if not l1 and not l2 and not carry:
                return None

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            node = ListNode(total % 10)

            node.next = add_with_carry(
                l1.next if l1 else None, l2.next if l2 else None, carry
            )
            return node

        return add_with_carry(l1, l2, 0)


if __name__ == "__main__":
    # Example
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    res = Solution().addTwoNumbers(l1, l2)
    print(res.val)
    print(res.next.val)
    print(res.next.next.val)

# coding=utf-8
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        这道题本质上是进行两个整数的加法运算。思路是采用递归算法，将 Node 值相加。
        若两个 Node 值相加大于 10，则他们下一 Node 的值相加之后，再加 1。
        :rtype: object
        :param l1:
        :param l2:
        """
        if l1 is None:
            l1 = ListNode(0)
        if l2 is None:
            l2 = ListNode(0)

        s = ListNode(l1.val + l2.val)
        tmp = ListNode(0)

        if s.val >= 10:
            s.val -= 10
            tmp = ListNode(1)

        # 若两者均没有 next node，则没有递归的必要了
        if (l1.next is not None) or (l2.next is not None):
            s.next = self.addTwoNumbers(l1.next, l2.next)

        if tmp.val != 0:
            s.next = self.addTwoNumbers(tmp, s.next)

        return s

# Usage

print("====example1:===")

a = ListNode(5)
a2 = ListNode(5)
r = Solution().addTwoNumbers(a, a2)
print r.val
print r.next.val

print("====example2:===")

a = ListNode(2)
b = ListNode(4)
# c = ListNode(3)
a.next = b
# b.next = c

a2 = ListNode(5)
b2 = ListNode(6)
# c2 = ListNode(4)
a2.next = b2
# b2.next = c2

sol = Solution()
r = sol.addTwoNumbers(a, a2)
print r.val

r2 = r.next
print r.next.val

if r2.next is not None:
    print r2.next.val

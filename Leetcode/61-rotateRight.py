# encoding: utf-8
#
# ###################
# 61. Rotate List
# Difficulty:Medium
# ###################
#
# Given a linked list, rotate the list to the right by k places, where k is non-negative.
#
# Example 1:
#
# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL
# Example 2:
#
# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL

import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None
        elif head.next is None or k == 0:
            return head

        node_list = []
        node = head

        while node.val is not None:
            node_list.append(node.val)

            if node.next is not None:
                node = node.next
            else:
                break

        len_node_list = len(node_list)

        if k < len_node_list:
            node_list = node_list[-k:] + node_list[:len_node_list-k]
        elif k == len_node_list or k % len_node_list == 0:
            return head
        else:
            m = k % len_node_list
            node_list = node_list[-m:] + node_list[:len_node_list-m]

        # 将列表转化为节点对象
        if len_node_list != 0:
            node = ListNode(node_list[0])
            if len_node_list > 1:
                tmp_node = node
                for i in range(1, len_node_list):
                    n = ListNode(node_list[i])
                    tmp_node.next = n
                    tmp_node = n
            return node
        else:
            return None

# leetcode.com Submission
# 231 / 231 test cases passed.
# Status: Accepted
# Runtime: 44 ms
# Your runtime beats 66.58 % of python3 submissions.


class SolutionTest(unittest.TestCase):
    def test_rotateRight1(self):
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node5 = ListNode(5)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        res = Solution().rotateRight(node1, 2)
        self.assertEqual(res.val, 4)

    def test_rotateRight2(self):
        node = ListNode(0)
        node1 = ListNode(1)
        node2 = ListNode(2)
        node.next = node1
        node1.next = node2
        res = Solution().rotateRight(node, 4)
        self.assertEqual(res.val, 2)
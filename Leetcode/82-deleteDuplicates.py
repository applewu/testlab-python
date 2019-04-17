# encoding: utf-8
#
# ###################
# 82. Remove Duplicates from Sorted List II
# Difficulty:Medium
# ###################
#
# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
#
# Example 1:
#
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
# Example 2:
#
# Input: 1->1->1->2->3
# Output: 2->3

# leetcode.com Submission
# 168 / 168 test cases passed.
# Status: Accepted
# Runtime: 52 ms
# Your runtime beats 53.87 % of python3 submissions.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        # 读取节点到列表中。
        node_list = []
        node = head
        duplicates = []

        if node is None:
            return None

        while node.val is not None:

            if node.val not in node_list:
                if node.val not in duplicates:
                    node_list.append(node.val)
            else:
                node_list.remove(node.val)
                duplicates.append(node.val)

            # 如果没有子节点，则跳出循环
            if node.next is not None:
                node = node.next
            else:
                break

        # 将列表转化为节点对象
        len_node_list = len(node_list)
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

node1 = ListNode(1)

Solution().deleteDuplicates(node1)

# example-1
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(3)
node5 = ListNode(4)
node6 = ListNode(4)
node7 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

Solution().deleteDuplicates(node1)

# example-2
node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(1)
node4 = ListNode(2)
node5 = ListNode(3)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

Solution().deleteDuplicates(node1)


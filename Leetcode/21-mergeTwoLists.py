# encoding: utf-8
# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        思路：利用自带的 sorted 方法，将 listnode 对象转化为数组进行合并排序，之后再转化为 listnode 输出
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        else:
            array1 = []
            array2 = []
            self.listnode2array(l1, array1)
            self.listnode2array(l2, array2)
            array = sorted(array1 + array2)
            merge_node = ListNode(array[0])
            self.array2listnode(array, merge_node)
            return merge_node

    def listnode2array(self, list_node, array):
        if list_node is not None:
            array.append(list_node.val)
            if list_node.next is not None:
                self.listnode2array(list_node.next, array)

    def array2listnode(self, array, list_node):
        if len(array) > 1:
            sec_node = ListNode(array[1])
            list_node.next = sec_node
            array.remove(array[0])
            self.array2listnode(array, sec_node)
        elif len(array) == 1:
            list_node.next = None

# listnode 对象转化为数组
a = ListNode(1)
b = ListNode(2)
c = ListNode(4)
a.next = b
b.next = c

result = []
Solution().listnode2array(a, result)
print result

# 数组转化为 listnode 对象
abc = ListNode(1)
Solution().array2listnode([1, 3, 4], abc)
print abc

a1 = ListNode(1)
b1 = ListNode(3)
c1 = ListNode(4)
a1.next = b1
b1.next = c1

# Usage
Solution().mergeTwoLists(a, a1)
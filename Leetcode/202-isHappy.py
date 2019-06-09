# encoding: utf-8
#
# ###################
# 202. Happy Number
# Difficulty:Easy
# ###################
#
# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
#
# Example:
#
# Input: 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

import unittest


class Solution:

    def isHappy(self, n: int) -> bool:
        if n == 0:
            return False
        elif n == 1:
            return True
        elif n > 1:
            return self.process(n, [])

    def process(self, n, processed):
        """
        这道题做得很顺利，可能因为留意到题目的 related topic 是 hash table :)

        401 / 401 test cases passed.
        Status: Accepted
        Runtime: 36 ms
        Memory Usage: 13.1 MB
        Your runtime beats 95.25 % of python3 submissions.

        :param n:
        :param processed:
        :return:
        """
        squares = {"1": 1, "2": 4, "3": 9, "4": 16, "5": 25, "6": 36, "7": 49, "8": 64, "9": 81, "0": 0}
        str_n = str(n)
        tmp = 0
        processed.append(n)
        for i in range(len(str_n)):
            tmp += squares[str_n[i]]

        if tmp == 1:
            return True
        elif tmp in processed:
            return False
        else:
            return self.process(tmp, processed)


class SolutionTest(unittest.TestCase):
    def test_rob(self):
        self.assertEqual(Solution().isHappy(19), True)
        self.assertEqual(Solution().isHappy(1), True)
        self.assertEqual(Solution().isHappy(99), False)
        self.assertEqual(Solution().isHappy(201), False)
        self.assertEqual(Solution().isHappy(176), True)
        self.assertEqual(Solution().isHappy(13), True)

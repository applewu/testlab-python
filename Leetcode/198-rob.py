# encoding: utf-8
#
# ###################
# 198. House Robber
# Difficulty:Easy
# ###################
#
# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and
# it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police.
#
# Example 1:
#
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
#
# Example 2:
#
# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
import unittest
from typing import List


class Solution:
    def rob1(self, nums: List[int]) -> int:

        """
        找规律，采用递归方法，结果是 Time Limit Exceeded
        超时原因是 n-2 方法会处理了两次，比如 rob(4) 就是依赖 rob(3) 和 rob(2) 的结果，而 rob(3) 本身也依赖 rob(2) 结果，明明是已知结果处理了多次
        :param nums:
        :return:
        """
        len_nums = len(nums)

        if len_nums == 0:
            return 0
        elif len_nums == 1:
            return nums[0]
        elif len_nums == 2:
            return max(nums)
        elif len_nums > 2:
            return max(self.rob1(nums[0:-2]) + nums[-1], self.rob1(nums[0:-1]))

    def rob(self, nums: List[int]) -> int:
        """
        由上述的递归方法优化为动态规划方法。把 rob(n-2) 和 rob(n-1) 的结果存在变量中。
        # 69 / 69 test cases passed.
        # Status: Accepted
        # Runtime: 32 ms
        # Memory Usage: 13 MB
        # Your runtime beats 94.42 % of python3 submissions.

        :param nums:
        :return:
        """
        len_nums = len(nums)

        if len_nums == 0:
            return 0

        dp1 = 0
        dp2 = 0

        for i in range(len_nums):
            dp = max(dp2 + nums[i], dp1)
            dp2 = dp1
            dp1 = dp

        return dp1


# 递归是从问题的最终目标出发，逐渐将复杂问题化为简单问题，最终求得问题是逆向的。
# 递推是从简单问题出发，一步步的向前发展，最终求得问题。是正向的。
# 一般来说，递推的效率高于递归（当然是递推可以计算的情况下）

class SolutionTest(unittest.TestCase):
    def test_rob(self):
        self.assertEqual(Solution().rob([1, 2, 3, 1]), 4)
        self.assertEqual(Solution().rob([2, 7, 9, 3, 1]), 12)
        self.assertEqual(Solution().rob([1, 20, 7, 9, 88, 1]), 108)
        self.assertEqual(Solution().rob([2]), 2)
        self.assertEqual(Solution().rob([]), 0)
        self.assertEqual(Solution().rob([1, 2, 34, 456, 1, 23, 79, 456, 9, 0, 1]), 938)
        self.assertEqual(Solution().rob([1, 2, 34, 456, 1, 23, 79, 26, 9, 0, 1]), 547)
        self.assertEqual(Solution().rob([4, 1, 2, 7, 5, 1, 3]), 14)
        self.assertEqual(Solution().rob([4, 1, 2, 7, 5, 3, 1]), 14)
        self.assertEqual(Solution().rob([8, 9, 9, 4, 10, 5, 6, 9, 7, 9]), 45)
        self.assertEqual(Solution().rob([8, 9, 9, 4, 10, 5, 6, 9, 7, 9, 11, 8]), 53)
        self.assertEqual(Solution().rob([1, 1, 3, 6, 7, 10]), 17)
        self.assertEqual(Solution().rob([1, 1, 3, 6, 7, 10, 7, 1, 8, 5, 9, 1, 4, 4, 3]), 42)





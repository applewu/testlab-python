# encoding: utf-8
#
# ###################
# 162. Find Peak Element
# Difficulty:Medium
# ###################
#
# A peak element is an element that is greater than its neighbors.
#
# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
#
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
#
# You may imagine that nums[-1] = nums[n] = -∞.
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:
#
# Input: nums = [1,2,1,3,5,6,4]
# Output: 1 or 5
# Explanation: Your function can return either index number 1 where the peak element is 2,
# or index number 5 where the peak element is 6.
# Note:
#
# Your solution should be in logarithmic complexity.

import unittest
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            return 0
        else:
            if nums[len(nums)-1] > nums[len(nums)-2]:
                return len(nums)-1

            for i in range(len(nums)-1):
                if nums[i] > nums[i + 1]:
                    return i
                elif nums[i] < nums[i + 1]:
                    continue
                else:
                    return None

# leetcode.com Submission
# 59 / 59 test cases passed.
# Status: Accepted
# Runtime: 32 ms
# Your runtime beats 93.03 % of python3 submissions.


class SolutionTest(unittest.TestCase):
    def test_findPeakElement(self):
        self.assertEqual(Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4]), 1)
        self.assertEqual(Solution().findPeakElement([1, 2, 3, 1]), 2)
        self.assertEqual(Solution().findPeakElement([1, 0, 5, 9, 8]), 0)
        self.assertEqual(Solution().findPeakElement([1, 2, 5]), 2)


# encoding: utf-8
#
# ###################
# 53. Maximum Subarray
# Difficulty: Easy
# ###################
#
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


class Solution:
    def maxSubArray(self, nums):
        """
        解题思路：之前没专门看过算法，对于动态规划也不了解，原来找到小问题到大问题之间的递推关系就是常见的动态规划思考方式。
        动态规划解题的四个步骤：1. 划分阶段；2. 确定状态和状态变量；3. 确定决策方法和状态转移方程；4. 为状态转移方程确定终止或边界条件
        maxSubArray(A, i) = maxSubArray(A, i - 1) > 0 ? maxSubArray(A, i - 1): 0 + A[i];
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length < 1:
            return 0
        result, max_num = nums[0], nums[0]
        for i in range(1, length):
            if max_num < 0:
                max_num = nums[i]
            else:
                max_num += nums[i]
            if max_num > result:
                result = max_num

        return result

# leetcode.com Submission
# 202 / 202 test cases passed.
# Status: Accepted
# Runtime: 40 ms
# Your runtime beats 100.00 % of python3 submissions.


# 4
print(Solution().maxSubArray([-1, 2, 1, -5, 4]))
# 6
print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
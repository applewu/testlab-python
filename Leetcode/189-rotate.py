# encoding: utf-8
#
# ###################
# 189. Rotate Array
# Difficulty:Easy
# ###################
#
# Given an array, rotate the array to the right by k steps, where k is non-negative.
#
# Example 1:
#
# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# 
# Example 2:
#
# Input: [-1,-100,3,99] and k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]


class Solution:
    def rotate(self, nums, k):
        """
        思路：这一题的逻辑很简单，关键在于要考虑多种情况。对于 k 是正数且小于 nums 长度的情况下，直接通过切片把前后的元素位置换掉，后面换到前面去。k 是负数的情况下，就是前面的数换到后面去。
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2 or k == 0:
            pass
        elif k > 0:
            len_nums_tmp = len(nums)
            if k > len_nums_tmp:
                k = k % len_nums_tmp
            elif k == len_nums_tmp:
                self.rotate(nums, 0)

            nums += nums[:len_nums_tmp - k]
            for ki in range(len_nums_tmp - k):
                nums.pop(0)
        elif k < 0:
            # k 是负数才会走到这个分支
            nums += nums[:-k]
            for ki in range(-k):
                nums.pop(0)

# leetcode.com Submission
# 34 / 34  test cases passed.
# Status: Accepted
# Runtime: 76   ms
# Your runtime beats 34.66 % of python3 submissions.

# [2, 1]
nums = [1, 2]
Solution().rotate(nums, 3)
print(nums)

# [2, 3, 4, 5, 6, 7, 1]
nums = [1, 2, 3, 4, 5, 6, 7]
Solution().rotate(nums, -1)
print(nums)

# [3, 99, -100, -1]
nums = [-1, -100, 3, 99]
Solution().rotate(nums, 2)
print(nums)

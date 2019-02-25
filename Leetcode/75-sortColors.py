# encoding: utf-8
#
# ###################
# 75. Sort Colors
# Difficulty:Medium
# ###################
# 
# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# Note: You are not suppose to use the library's sort function for this problem.

# Example:

# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Follow up:

# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.

		leetcode.com Submission
        87 / 87 test cases passed.
        Status: Accepted
        Runtime: 20 ms
        Your runtime beats 100.00 % of python submissions.

        """
        if len(nums) > 1:
            init_nums = nums[:]

            del nums[:]

            for n in init_nums:
                if n == 0:
                    nums.insert(0, n)
                elif n == 2:
                    nums.append(n)
                elif n == 1:
                    if 2 in nums:
                        index = nums.index(2)
                        nums.insert(index, n)
                    else:
                        nums.append(n)

nums = [2,0,2,1,1,0]
print("Before:")
print(nums)
Solution().sortColors(nums)
print("After:")
print(nums)
 
# encoding:utf-8
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# Example 1:
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1


class Solution(object):
    def search(self, nums, target):
        """
        思路：不想采用 python 自带的查找方法。自己进行逻辑判断来处理。
        :param nums:
        :param target:
        :return:
        """

        # 对于空数组，或数组长度为 1,2 的情况进行特殊处理
        if len(nums) == 0:
            return -1
        else:
            if nums[len(nums) - 1] == target:
                return len(nums) - 1
            elif nums[0] == target:
                return 0
            elif (len(nums) == 1) | (len(nums) == 2):
                return -1

        # 先找出真正的旋转中心点
        pivot_index = 0
        for i in range(pivot_index, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                pivot_index = i
                break
            else:
                i += 1

        # 根据中心点，将原来的数组分两小段处理。由于两小段都是升序的，比对大小来确定 target 在前段还是后段
        offset = 0
        if target == nums[pivot_index]:
            return pivot_index
        elif (target > nums[0]) & (target < nums[pivot_index]):
            array = nums[:pivot_index + 1]
        elif (target >= nums[pivot_index + 1]) & (target < nums[len(nums) - 1]):
            array = nums[pivot_index + 1:]
            offset = pivot_index + 1
        else:
            return -1

        for n in range(len(array)):
            if array[n] == target:
                return n + offset
            elif n == len(array) - 1:
                return -1
            else:
                n += 1

    def search1(self, nums, target):
        """
        算是个反面教材吧，虽然被 leetcode 站点接受答案了，哈哈 :)
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target not in nums:
            return -1
        else:
            return nums.index(target)


print(Solution().search([1, 3], 0))
print(Solution().search([1, 3], 1))
print(Solution().search([1, 3], 3))
print(Solution().search([1, 3, 5], 0))
print(Solution().search([1, 2, 3, 4, 5, 6, 7, 0], 8))
print(Solution().search([8, 1, 2, 3, 4, 5, 6, 7], 6))
print(Solution().search([3, 4, 5, 6, 7, 1, 2], 4))
print(Solution().search([4, 5, 6, 0, 1, 2], 6))
print(Solution().search([4, 5, 6, 7, 0, 1, 2], 5))
print(Solution().search([5, 6, 7, 1, 3], 1))
print(Solution().search([1, 3, 5, 6], 1))
print(Solution().search([1, 3, 5], 1))
print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
print(Solution().search([4, 5, 6, 7, 0, 1, 2], 3))
print(Solution().search1([4, 5, 6, 7, 0, 1, 2], 0))
print(Solution().search1([4, 5, 6, 7, 0, 1, 2], 3))

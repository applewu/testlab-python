# coding=utf-8
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution(object):
    def twoSum(self, nums, target):
        """
        思路：先找到 nums 中合适的元素，再输出它们在数组中的位置
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        i = 0
        j = len(nums) - 1
        result = []  # 记录 nums 中合适的数字元素
        result_index = []  # 记录 nums 中合适的数字元素的位置
        sorted_nums = sorted(nums)
        while i < j:
            if target == sorted_nums[i] + sorted_nums[j]:
                result.append(sorted_nums[i])
                result.append(sorted_nums[j])
                break
            elif sorted_nums[i] + sorted_nums[j] < target:
                i += 1
            elif sorted_nums[i] + sorted_nums[j] > target:
                j -= 1

        result_index.append(nums.index(result[0]))
        # 为了应对 result 中元素相同的情况，第二个数字从 nums 后面往前查找
        result_index.append(len(nums)-nums[::-1].index(result[1])-1)

        return result_index


nums = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(nums, target))

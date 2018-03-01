# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


def ex_sum(nums, target):
    i = 0
    j = len(nums) - 1
    result = []
    sorted_nums = sorted(nums)
    while i < j:
        if target == sorted_nums[i] + sorted_nums[j]:
            result.append(sorted_nums[i])
            result.append(sorted_nums[j])
            return result
        elif sorted_nums[i] + sorted_nums[j] < target:
            i += 1
        elif sorted_nums[i] + sorted_nums[j] > target:
            j -= 1


print ex_sum([1, 2, 7, 8, 4], 5)

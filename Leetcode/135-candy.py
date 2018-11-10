# encoding: utf-8
#
# ###################
# 135. Candy
# Difficulty:Hard
# ###################
#
# There are N children standing in a line. Each child is assigned a rating value.
#
# You are giving candies to these children subjected to the following requirements:
#
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?
#
# Example 1:
#
# Input: [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
# Example 2:
#
# Input: [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
#              The third child gets 1 candy because it satisfies the above two conditions.


class Solution:
    def candy(self, ratings):
        """
        思路：这一题的关键是考虑前面已经计算过的 child candy 还需要补发。
        :type ratings: List[int]
        :rtype: int
        """
        if len(ratings) == 0:
            return 0
        elif len(ratings) == 1:
            return 1
        elif len(ratings) >= 2:
            candy = 1

            # 需要记录前一个数字得到的 candy 数量
            # 如果当前的数字大于前一个，那么当前获得的 candy 是前一个数字对应 candy + 1
            # 如果相等，则当前获得的 candy 是 1
            # 如果小于前一个数字，且对应的 candy 数量不小于前一个数字的 candy，那么当前 child 获得的 candy 是 1，candy 总数还需增加，需要给前面较大的 child 补发 candy
            left_is_more = []
            pre_count = 1
            for i in range(1, len(ratings)):
                if ratings[i] > ratings[i - 1]:
                    count = pre_count + 1

                    # 清算 left_is_more 的过程就是要补发 candy，left_is_more 是倒序的，记录了 child rating value，相应的 candy
                    if len(left_is_more) > 0:

                        # 因为进入 left_is_more 就说明 i -2 大于 i-1 的 child
                        # 走到这里，又说明 i 大于 i-1 的 child，说明 i-1 是 i 和 i-2 之间最小的数字
                        len_left_more = len(left_is_more)
                        last = left_is_more[len_left_more - 1]
                        last_key = list(last.keys())[0]
                        # pre_count 就是 i -1 的 child candy
                        if last[last_key] < pre_count:
                            last[last_key] += 1
                            candy += 1
                        elif last[last_key] == pre_count and ratings[i - 2] > ratings[i - 1]:
                            last[last_key] += 1
                            candy += 1

                        if len(left_is_more) > 1:
                            # 从后往前清算, left_is_more 数组的最后两个数字开始比较
                            #
                            for j in range(len_left_more, 0, -1):
                                # 倒数的两个个数字
                                k1 = list(left_is_more[j - 2].keys())[0]
                                k2 = list(left_is_more[j - 1].keys())[0]
                                v1 = left_is_more[j - 2][k1]
                                v2 = left_is_more[j - 1][k2]

                                # 既然 k1 在 k2 之前，这是倒序数组，所以 v1 应该大于 v2，否则 v1 就应该是 v2 加 1
                                if int(k1) > int(k2) and v1 <= v2:
                                    left_is_more[j - 2][k1] = v2 + 1
                                    candy += v2 + 1 - v1

                    left_is_more = []

                else:
                    count = 1

                    # 比左边的数字小，把左边的数字加入到 left_is_more 数组中
                    # 若两者相等，存在 left_is_more 无需清算，把数字记录下来
                    if ratings[i] <= ratings[i - 1]:
                        left_is_more.append({str(ratings[i - 1]): pre_count})

                    len_left_more = len(left_is_more)
                    # 如果 i 是最后一个 rating 元素，就需要立刻清算，否则会等到下一个循环清算
                    if i == len(ratings) - 1 and len_left_more > 0:
                        last = left_is_more[len_left_more - 1]
                        k = list(last.keys())[0]
                        v = last[k]
                        if ratings[i] < int(k) and count >= v:
                            last[k] = count + 1
                            candy += last[k] - v

                        if len(left_is_more) > 1:
                            # 从后往前清算, left_is_more 数组的最后两个数字开始比较
                            for j in range(len_left_more, 0, -1):
                                # 倒数的两个个数字
                                k1 = list(left_is_more[j - 2].keys())[0]
                                k2 = list(left_is_more[j - 1].keys())[0]
                                v1 = left_is_more[j - 2][k1]
                                v2 = left_is_more[j - 1][k2]

                                # 既然 k1 在 k2 之前，这是倒序数组，所以 v1 应该大于 v2，否则 v1 就应该是 v2 加 1
                                if int(k1) > int(k2) and v1 <= v2:
                                    left_is_more[j - 2][k1] = v2 + 1
                                    candy += v2 + 1 - v1

                candy += count
                pre_count = count

            return candy

# leetcode.com Submission
# 48 / 48 test cases passed.
# Status: Accepted
# Runtime: 204  ms
# Your runtime beats 5.01 % of python3 submissions.

# 31
print(Solution().candy([1, 2, 3, 5, 4, 3, 2, 1, 4, 3, 2, 1]))
# 13
print(Solution().candy([1, 2, 87, 87, 87, 2, 1]))
# 23
print(Solution().candy([9, 9, 2, 6, 2, 4, 3, 11, 23, 67, 21, 10, 10]))
# 37
print(Solution().candy([1, 0, 2, 4, 3, 2, 5, 7, 4, 6, 1, 0, 9, 2, 6, 2, 4, 3, 11, 23]))
# 11
print(Solution().candy([3, 2, 2, 1, 0, 2]))
# 34
print(Solution().candy([1, 0, 2, 4, 3, 2, 5, 7, 4, 6, 3, 2, 1, 0, 2]))
# 1
print(Solution().candy([1]))
# 13
print(Solution().candy([1, 0, 2, 4, 3, 2, 5]))
# 5
print(Solution().candy([1, 0, 2]))
# 4
print(Solution().candy([1, 2, 2]))

# encoding: utf-8
# The count-and-say sequence is the sequence of integers with the first five terms as following:
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth term of the count-and-say sequence.
#
# Note: Each term of the sequence of integers will be represented as a string.
#
# Example 1:
#
# Input: 1
# Output: "1"
# Example 2:
#
# Input: 4
# Output: "1211"


class Solution(object):
    def countAndSay(self, n):
        """
        思路：下一个数的结果是根据上一个的值推理出来的，所以采用递归
        :type n: int
        :rtype: str
        """
        if n == 1:
            return str(1)
        count = 1
        seq = self.countAndSay(n - 1)
        if len(seq) == 1:
            return str(count) + seq

        i = 1
        result = ''
        while i < len(seq):
            if seq[i] == seq[i - 1]:
                count += 1
                if i + 1 == len(seq):
                    result += str(count) + seq[i - 1]
            else:
                result += str(count) + seq[i - 1]
                count = 1
                if i + 1 == len(seq):
                    result += str(count) + seq[i]
            i += 1
        return result


print Solution().countAndSay(1)
print Solution().countAndSay(2)
print Solution().countAndSay(3)
print Solution().countAndSay(4)
print Solution().countAndSay(5)



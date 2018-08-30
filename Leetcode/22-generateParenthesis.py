# encoding:utf-8
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.parenthesis(n, '', 0, 0, result)
        return result

    def parenthesis(self, n, str, left, right, result):
        if len(str) == n*2:
            result.append(str)
        if left < n:
            self.parenthesis(n, str + '(', left + 1, right, result)
        if right < left:
            self.parenthesis(n, str + ')', left, right + 1, result)


print Solution().generateParenthesis(3)
print Solution().generateParenthesis(100)

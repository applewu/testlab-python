# encoding: utf-8
#
# ###################
# 224. Basic Calculator
# Difficulty:Hard
# ###################
#
# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .
#
# Example 1:
#
# Input: "1 + 1"
# Output: 2
# Example 2:
#
# Input: " 2-1 + 2 "
# Output: 3
# Example 3:
#
# Input: "(1+(4+5+2)-3)+(6+8)"
# Output: 23
# Note:
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.

from queue import Queue


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def clear(self):
        self.items = []


class Solution:
    def calculate(self, s: str) -> int:
        """
        对可能带有括号、空格的加减运算表达式进行计算。
        思路：使用栈来处理括号表达式的问题。对于不存在括号的表达式，就可以通过队列，从左到右进行计算。重点关注负数的处理。
        我这里的实现还是太累赘了，中间处理还是用了字符串，导致很多 for 循环去获取数字和表达式。中间处理用列表应该更好些。
        :param s: 可能带有括号的加减运算表达式
        :return: 计算得出的数字结果
        """
        s = s.replace(" ", "")

        if "(" not in s and ")" not in s:
            return self.cal_without_brackets(s)
        else:
            # 有括号就意味着运算的次序就收到影响，所以用到栈的先进后出
            s_stack = Stack()
            str_expression = ''
            for i in range(len(s)):
                s_stack.push(s[i])
                if s[i] == ")":
                    while not s_stack.items[-1] == "(":
                        str_expression += s_stack.pop()
                    # 括号内的表达式的值已经计算出来了，最初的表达式中不需要有左括号了
                    s_stack.pop()

                    # 注意表达式字符串的顺序，上面的处理是从右往左，这里要转成从左往右
                    str_expression_real = ''
                    for j in range(len(str_expression) - 1, 0, -1):
                        str_expression_real += str_expression[j]

                    number = self.cal_without_brackets(str_expression_real)
                    str_num = str(number)
                    if len(str_num) > 1:
                        # 如果是第一个数字且是负数，那么就无需理会数字前面的正负号的处理
                        if len(s_stack.items) == 0 and number < 0:
                            for n in range(len(str_num)):
                                s_stack.push(str_num[n])
                        else:
                            for n in range(len(str_num)):
                                # 处理 number 是负数的情况
                                if number < 0 and s_stack.items[-1] == "+" and str_num[n] == "-":
                                    s_stack.pop()
                                    s_stack.push(str_num[n])
                                elif number < 0 and s_stack.items[-1] == "-" and str_num[n] == "-":
                                    s_stack.pop()
                                    s_stack.push("+")
                                else:
                                    s_stack.push(str_num[n])
                    else:
                        s_stack.push(str_num)
                    str_expression = ''

            # 已经没有括号问题了，如果 stack 数组长度大于2，就作为表达式处理，从左到右
            if len(s_stack.items) == 3 and s_stack.items[1] in ("+", "-"):
                return self.plus_or_minus(s_stack.items[1], int(s_stack.items[0]), int(s_stack.items[2]))
            elif len(s_stack.items) == 1:
                return int(s_stack.items[0])
            else:
                for k in range(len(s_stack.items)):
                    str_expression += s_stack.items[k]
                return self.cal_without_brackets(str_expression)

    def plus_or_minus(self, symbol, left, right):
        """
        两个数字的加减运算
        :param symbol: 本题中运算符仅有 +, -
        :param left: 表达式左边的数字
        :param right: 表达式右边的数字
        :return:
        """
        if symbol == '+':
            return left + right
        elif symbol == '-':
            return left - right

    def cal_without_brackets(self, s):
        """
        根据字符串类型的表达式，计算结果
        :param s: 不包含括号的字符串类型的表达式
        :return: 表达式的数字结果
        """
        if "+" not in s and "-" not in s:
            return int(s)
        elif (s.split("+")[0] == "" or s.split("-")[0] == "") and ("+" not in s[1:] and "-" not in s[1:]):
            return int(s)

        # 获得完整数字
        q = Queue()
        # 获得要进行加减法的表达式
        expression = []
        str_number = ''

        for i in range(len(s)):
            if s[i] in ("+", "-") and i != 0:
                # 说明数字字符串结束了，把队列中的数字整合起来，形成完整的数字，数字要追加在表达式中
                # 还有一种情况是，待计算表达式的第一个数字是负数，所以第一个字符会出现 "-", 此时 str_number 为空，不应该追加到 expression
                while not q.empty():
                    str_number += q.get()
                expression.append(str_number)

                # 表达式中如果只有一个数字，就可以把运算符加入
                if len(expression) == 1:
                    expression.append(s[i])

                # 形成完整数字之后，队列就可以清空，临时的数字字符串也可以重置了
                q.empty()
                str_number = ''
            else:
                q.put(s[i])

                # 如果是最后一个数字，直接算在表达式中；否则的话，不能草率追加到表达式中。因为这个数字字符串还未结束。
                if i == len(s) - 1:
                    while not q.empty():
                        str_number += q.get()
                    expression.append(str_number)

            if len(expression) == 3:
                res = self.plus_or_minus(expression[1], int(expression[0]), int(expression[2]))
                # 如果表达式还没有结束，说明后面还有运算，进行递归处理
                if len(s[i:]) > 1:
                    return self.cal_without_brackets(str(res) + s[i:])
                else:
                    return res

# leetcode.com Submission
# 37 / 37 test cases passed.
# Status: Accepted
# Runtime: 3692 ms, faster than 5.02% of Python3 online submissions for Basic Calculator.
# Memory Usage: 18.4 MB, less than 6.38% of Python3 online submissions for Basic Calculator.


print(Solution().calculate(s="4-5+2"))
print(Solution().calculate(s="1+(4+51+2)-3"))
print(Solution().calculate(s="2-1 + 2"))
print(Solution().calculate(s="(1+(4+51+2)-3)+(6+8)"))
print(Solution().calculate(s="(154)"))
print(Solution().calculate(s="(154)-4"))
print(Solution().calculate(s="(-1213)"))
print(Solution().calculate(s="(1+(4+5+2)-3)+(6+8)+(10-243)"))
print(Solution().calculate(s="(1+(4+5+2)-3)+(6+8)+(10-23)"))
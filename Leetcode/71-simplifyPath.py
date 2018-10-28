# encoding: utf-8
# Given an absolute path for a file (Unix-style), simplify it.
#
# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
# path = "/a/../../b/../c//.//", => "/c"
# path = "/a//b////c/d//././/..", => "/a/b/c"
#
# In a UNIX-style file system, a period ('.') refers to the current directory, so it can be ignored in a simplified path. Additionally, a double period ("..") moves up a directory, so it cancels out whatever the last directory was. For more information, look here: https://en.wikipedia.org/wiki/Path_(computing)#Unix_style
#
# Corner Cases:
#
# Did you consider the case where path = "/../"?
# In this case, you should return "/".
# Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
# In this case, you should ignore redundant slashes and return "/home/foo".


class Solution:
    def simplifyPath(self, path):
        """
        思路：这道题难点在于需要考虑全面，留意到题干指出的 "//", "/..", "/./" 情况还不够，还需要考虑 "/...", 以及结尾是 "/." 的情况。
        :type path: str
        :rtype: str

        leetcode.com Submission
        252 / 252 test cases passed.
        Status: Accepted
        Runtime: 48 ms
        Your runtime beats 58.46 % of python3 submissions.
        """

        if path is None or len(path) == 0:
            return '/'
        elif path == '/.':
            return '/'
        elif path[-1] == '/' and len(path) >= 2:
            if path[-2] != '/':
                return self.simplifyPath(path[:-1])
        elif '/' != path[0]:
            return self.simplifyPath('/' + path)

        # 若以 "/." 结尾，那么结尾的 "/." 可忽略
        if path[-1] == '.' and len(path) >= 2:
            if path[-2] == '/':
                return self.simplifyPath(path[:-2])

        if '//' in path and len(path) > 2:
            return self.simplifyPath(path.replace('//', '/'))

        if '.' not in path:
            # path 中不存在 "." 不存在 "//"，那么可以直接返回
            if '//' not in path:
                return path
            elif '//' in path and len(path) == 2:
                return '/'
        elif '/./' in path:
            return self.simplifyPath(path.replace('/./', '/'))
        # path 中不存在 ".." 存在 "."，那么 "./" 可忽略
        elif '..' not in path and './' in path:
            return self.simplifyPath(path.replace('./', ''))
        elif '/..' in path and len(path) == 3:
            return '/'
        # path 中存在 "/.."，至少长度到了 "/../a" 才有必要找上一级目录
        # 无需处理 /... 的情况，但需要处理 /..
        elif (('/..' in path and path[-3:] == '/..') or ('/../' in path)) and len(path) >= 5:
            # "/../" 转化为 "/"
            if path.index('/..') == path.index('/') and path.index('/') == 0:
                return self.simplifyPath(path[3:])
            # "/.." 不是 path 的开头
            elif path.index('/..') != 0:
                up_index = path.index('/..')
                up_dir_str = path[:up_index]

                # 路径字符串只有可能第一个目录是不带 / 的
                if '/' in up_dir_str:
                    ignore_start = up_dir_str.rindex('/')
                else:
                    ignore_start = 0

                if up_index == ignore_start + 1:
                    ignore_start -= 1
                    while ignore_start >= 0:
                        if path[ignore_start] == '/':
                            if ignore_start >= 1:
                                ignore_start -= 1
                            else:
                                ignore_start = 0
                                break
                        else:
                            break
                # ignore_str = path[ignore_start:up_index + 3]
                path = path[:ignore_start] + path[up_index + 3:]
                return self.simplifyPath(path)
        # 无需额外处理了，直接返回 path
        else:
            return path

# /
print(Solution().simplifyPath(path="///eHx/.."))

# /is
print(Solution().simplifyPath(path="/home/of/foo/../../bar/../../is/./here/.."))

# /is/here
print(Solution().simplifyPath(path="/home/of/foo/../../bar/../../is/./here/."))

# /abc/...
print(Solution().simplifyPath(path="/abc/..."))

# /abc/.../SDF/.../sdff
print(Solution().simplifyPath(path="/abc/.../SDF/.../sdff"))

# /a
print(Solution().simplifyPath(path="./a"))

# /a
print(Solution().simplifyPath(path="/a"))

# /abc
print(Solution().simplifyPath(path="./abc"))

# /abc
print(Solution().simplifyPath(path="abc"))

# /a
print(Solution().simplifyPath(path="../a/"))

# /
print(Solution().simplifyPath(path="../"))

# /
print(Solution().simplifyPath(path="/."))

# /e/f/g
print(Solution().simplifyPath(path="/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///"))

# /dfasdf
print(Solution().simplifyPath(path="abc/sfsdl/../../dfasdf/"))

# /home
print(Solution().simplifyPath(path='/home/'))

# /home/foo
print(Solution().simplifyPath(path='/home//foo/'))

# /c
print(Solution().simplifyPath(path='/a/./b/../../c/'))

# /c
print(Solution().simplifyPath(path='/a/../../b/../c//.//'))

# /a/b/c
print(Solution().simplifyPath(path='/a//b////c/d//././/..'))
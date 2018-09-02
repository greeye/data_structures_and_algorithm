# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
import collections
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst = []
        label = ''
        for i in s:
            lst.append(i)
        cc=collections.Counter(lst)
        dic=dict(cc)
        temp = []
        for k,v in dic.items():
            if v==1:
                label = k
                break
        if label == '':
            return -1
        for i in range(len(lst)):
            if lst[i] == label:
                return i
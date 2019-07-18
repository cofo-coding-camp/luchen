class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
        hash = {}
        n = len(s)
        result = 0
        for i in range(n-1):
            if s[i] not in hash:
                hash[s[i]] = True
            right = i + len(hash)
            while right < n and s[right] not in hash:
                hash[s[right]] = True
                right += 1 
            result = max(len(hash), result)
            del hash[s[i]]
        return result
# Solution using Counter
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique = Counter(s)
        for index, char in enumerate(s):
            if unique[char] == 1:
                return index
                break
        
        return -1
        

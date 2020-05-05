# can't use set since:
#   1. it is not iterable
#   2. it doesn't sort the in the original order

from collections import OrderedDict as od
# So use Ordered dict
def firstUniqChar(self, s: str) -> int:
        unique = od((x,"") for x in s)
        
        for key, value in unique.items():
            print(key)

s = 'loveleetcode'
firstUniqChar(s)
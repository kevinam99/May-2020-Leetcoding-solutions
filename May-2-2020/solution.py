# This is pretty easy in Python

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = [stones for stones in S if stones in J]
        return len(count)
class Solution:
    def findComplement(self, num: int) -> int:
        bin_num = bin(num)[2:]
        ans = ''
        for i in range(len(bin_num)):
            if bin_num[i] == '1': ans+= '0'
            if bin_num[i] == '0': ans+= '1'
        
        return int(ans, 2)
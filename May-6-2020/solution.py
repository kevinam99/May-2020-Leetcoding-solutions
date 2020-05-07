class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        new_list = Counter(nums)
        majority = len(nums) / 2 # given
        for occurence_count in new_list:
            if new_list[occurence_count] > majority:
                return occurence_count
                break
# used the Couter method from the previous day's problem
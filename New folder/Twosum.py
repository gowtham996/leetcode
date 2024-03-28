class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for idx,value in enumerate(nums):
            reqnum=target-value

            if reqnum in d:
                return [idx,d[reqnum]]
            else:
                d[value]=idx
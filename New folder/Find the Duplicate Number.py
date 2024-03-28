class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #  seen=set()
        #  for num in nums:
        #      if num in seen:
        #          return num
        #      seen.add(num)
        n = len(nums)
        nums.sort()  # Corrected line to invoke the sort method
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return nums[i]
        return len(nums)
        
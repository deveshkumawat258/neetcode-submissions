class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        n=0
        for _ in nums:
            n+=1
        for i in range(n):
            seen[nums[i]]=i
        for i in range(n):
            c=target-nums[i]
            if c in seen and seen[c]!=i:
                return[i,seen[c]]
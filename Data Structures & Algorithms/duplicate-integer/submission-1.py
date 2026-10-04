class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        r = set()
        x = 0
        for ele in nums:
            if ele in r:
                x = 1
                return True
            else:
                r.add(ele)
        if x == 0:
            return False
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums + nums
        return ans

s = Solution()
s.getConcatenation([1, 4, 6, 3, 4])
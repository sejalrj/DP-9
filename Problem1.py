class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        [10,9,2,5,3,7,101,18]
          1 1 1 
        """
        dp = [1]*len(nums)
        maxx = 0

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
        
        

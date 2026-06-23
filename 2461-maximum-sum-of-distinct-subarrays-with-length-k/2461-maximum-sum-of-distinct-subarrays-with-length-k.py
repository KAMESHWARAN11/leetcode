class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = {}
        window_sum = 0
        ans = 0

        # First window
        for i in range(k):
            window_sum += nums[i]
            freq[nums[i]] = freq.get(nums[i], 0) + 1

        if len(freq) == k:
            ans = window_sum

        # Slide the window
        for i in range(k, len(nums)):
            outgoing = nums[i - k]
            freq[outgoing] -= 1

            if freq[outgoing] == 0:
                del freq[outgoing]

            window_sum -= outgoing

            incoming = nums[i]
            freq[incoming] = freq.get(incoming, 0) + 1
            window_sum += incoming

            if len(freq) == k:
                ans = max(ans, window_sum)

        return ans
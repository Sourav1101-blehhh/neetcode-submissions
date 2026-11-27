class Solution:
    from collections import defaultdict
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        sorted_nums = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)
        return sorted_nums[:k]
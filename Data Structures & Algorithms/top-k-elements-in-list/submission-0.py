class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        uniques = set(nums)
        counts = {}
        for num in uniques:
            counts[num] = nums.count(num)
        
        arr = []
        for num, count in counts.items():
            arr.append([count, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
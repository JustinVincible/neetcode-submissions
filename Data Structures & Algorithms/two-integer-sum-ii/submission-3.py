class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        seen = {}
        for i, num in enumerate(numbers):
            tar = target - num
            if tar in seen:
                return [seen[tar]+1, i+1]
            seen[num] = i
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = 0
        seen = {}

        for i, num in enumerate(numbers):
            tar = target - num
            if tar in seen and seen[tar] is not i:
                return [seen[tar]+1, i+1]
            seen[num] = i
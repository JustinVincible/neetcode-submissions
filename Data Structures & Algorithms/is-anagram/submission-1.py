class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = {}
        dt = {}
        for char in s:
            if char in ds:
                ds[char] += 1
            else:
                ds[char] = 1
        for char in t:
            if char in ds:
                ds[char] -= 1
            else:
                return False
        
        for char in ds:
            if ds[char] != 0:
                return False
        return True
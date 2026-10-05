class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r"[^a-zA-Z0-9]","",s)
        print(s)
        print(s[::-1])
        if s == s[::-1]:
            return True
        else:
            return False
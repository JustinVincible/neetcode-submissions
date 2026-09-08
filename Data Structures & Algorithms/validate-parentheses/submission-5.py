class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        pairs = {
            '{':'}',
            '[':']',
            '(':')'
        }
        lefts = {
            '{':0,
            '[':0,
            '(':0
        }
        lefts = ['{', '[', '(']
        rights = ['}', ']', ')']
        seen = []
        for char in s:
            print(f"char {char}")
            if char in lefts:
                seen.append(char)
                print(f"seen {seen}")
            else:
                if len(seen) == 0 or char != pairs[seen[-1]]:
                    return False
                else:
                    seen.pop(-1)
        if len(seen) == 0:
            return True
        else:
            return False
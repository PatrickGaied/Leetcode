class Solution:
    def isValid(self, s: str) -> bool:
        lst = []

        def compat(r, k):
            return (r=='(' and k==')') or (r=='[' and k==']') or (r=='{' and k=='}')

        for p in s:
            if p in ['(', '[', '{']:
                lst.append(p)
            elif not lst or not compat(lst.pop(), p):
                return False

        return not lst
        
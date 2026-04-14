class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for log in logs:
            if log == '../':
                ans = (0 if ans <= 1 else ans - 1)
            elif log == './':
                continue
            else:
                ans += 1
        
        return ans
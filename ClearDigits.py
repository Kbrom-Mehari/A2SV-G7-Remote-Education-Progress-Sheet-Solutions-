class Solution:
    @staticmethod
    def clearDigits(s:str):
        stack=[]
        for ch in s:
            if ch.isdigit():
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)
        
          
    
print(Solution.clearDigits("cb4"))
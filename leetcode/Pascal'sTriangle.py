class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []

        for i in range(numRows):
            row = [1] * (i + 1)  
            
            for j in range(1, i):
                row[j] = output[i-1][j-1] + output[i-1][j]
            
            output.append(row)
        
        return output
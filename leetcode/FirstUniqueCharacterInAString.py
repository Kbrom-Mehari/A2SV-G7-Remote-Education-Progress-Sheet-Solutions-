class Solution:
    @staticmethod
    def firstUniqChar(string):
        frequency_map={}
        for s in string:
            frequency_map[s] = frequency_map.get(s,0) + 1  
                                                          
        for i in string:
            if frequency_map[i] == 1:
                return string.index(i)
        return -1
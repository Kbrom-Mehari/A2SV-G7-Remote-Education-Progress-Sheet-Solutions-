class Solution:
    @staticmethod
    def timeRequiredToBuy(tickets,k):
        target = tickets[k]
        seconds = 0
        for i in range(len(tickets)):
            if i <= k:
                seconds += min(target,tickets[i])
            else:
                seconds += min(target-1,tickets[i])
        return seconds
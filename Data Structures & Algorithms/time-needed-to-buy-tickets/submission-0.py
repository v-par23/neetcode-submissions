class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # time = 0
        # while True:
        #     for i in range(len(tickets)):
        #         if tickets[k] == 0:
        #             return time      

        #         if tickets[i] == 0:
        #             continue 
                    
        #         if tickets[i] >= 1:
        #             tickets[i] -= 1
        #             time += 1

        res = 0
        for i in range(len(tickets)):
            if i <= k:
                res += min(tickets[i], tickets[k])
            else:
                res += min(tickets[i], tickets[k] - 1)
        return res


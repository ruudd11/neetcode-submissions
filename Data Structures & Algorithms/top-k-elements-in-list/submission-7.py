class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        arry = []
        for n, c in count.items():
            arry.append([c,n])
        arry.sort()

        res = []
        while len(res) < k:
            res.append(arry.pop()[1])
        return res
        

            




        
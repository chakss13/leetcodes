from collections import Counter, defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       count = Counter(nums)
       print(count)
       b = list()
       common = count.most_common(k)
       result = [element for element, count in common]
       return result
        

    

        

        
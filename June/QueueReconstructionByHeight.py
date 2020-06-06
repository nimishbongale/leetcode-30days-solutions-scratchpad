class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ans = []
        k = sorted(people, key = lambda a: (-a[0], a[1]))
        for i in k:
            ans.insert(i[1], i)
        return ans

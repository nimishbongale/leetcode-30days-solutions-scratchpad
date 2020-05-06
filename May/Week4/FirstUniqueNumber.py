class FirstUnique:
    arr=[]
    stor={}
    def __init__(self, nums: List[int]):
        self.arr=nums
        self.stor=Counter(nums)
    def showFirstUnique(self) -> int:
        return list(self.stor.keys())[list(self.stor.values()).index(1)] if 1 in self.stor.values() else -1
    def add(self, value: int) -> None:
        self.arr.append(value)
        self.stor[value]=self.stor.get(value,0)+1
        
# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)

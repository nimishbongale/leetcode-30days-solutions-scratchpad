class LRUCache:
    lru,use={},[]
    cap=0
    def __init__(self, capacity: int):
        self.lru={}
        self.use=[]
        self.cap=capacity

    def get(self, key: int) -> int:
        if key in self.lru:
            self.use.remove(key)
            self.use.append(key)
            return self.lru[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            self.lru[key]=value
            self.use.remove(key)
            self.use.append(key)
            return
        elif len(self.lru)>=self.cap:
            self.lru.pop(self.use[0])
            self.use=self.use[1:]    
        self.lru[key]=value
        self.use.append(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

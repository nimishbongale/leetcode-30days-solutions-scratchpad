class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        make_heap(stones.begin(),stones.end());
        while(stones.size()>1){
        int y=stones.front();
        pop_heap(stones.begin(), stones.end());
        stones.pop_back();
        int x=stones.front();
        pop_heap(stones.begin(),stones.end());
        stones.pop_back();
        if(x!=y){
            stones.push_back(y-x);
            push_heap(stones.begin(),stones.end());
            }
        }
        if(stones.empty())
            return 0;
        return stones[0];
    }
};

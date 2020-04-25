class Solution {
public:
    bool canJump(vector<int>& nums) {
        int len=nums.size(),max1=0;
        for(int i=0;i<=max1;i++){
            max1=max(max1,i+nums[i]);
                if(max1>=len-1) return true;
        }
        return false;
    }
};

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if(nums.empty()) return 0;
        vector<int> max_sub_total(nums.size());
        max_sub_total[0] = nums[0];
        for(auto idx{1}; idx< nums.size(); ++idx)
            max_sub_total[idx] = max(max_sub_total[idx-1] + nums[idx], nums[idx]); 
        return  *max_element(max_sub_total.begin(),max_sub_total.end());
    }
};

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int cnt = 1;
        for(int i =1; i < n; i++){
            if(nums[i] == nums[i-1]){
                cnt++;
                if(cnt > (n/2)){
                    return nums[i];
                }
            }
            else{
                cnt = 1;
            }
        }
        return nums[n-1];
    }
};
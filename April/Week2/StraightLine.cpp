class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& c) {
        if(c.size()>2){
            long double m,temp;
            if(c[1][0]-c[0][0]!=0)
                m=(c[1][1]-c[0][1])/(c[1][0]-c[0][0]);
            else
                m=INT_MAX;
                for(int i=2;i<c.size();i++){
                if(c[i][0]-c[i-1][0]!=0)
                temp=(long double)(c[i][1]-c[i-1][1])/(c[i][0]-c[i-1][0]);
                else
                    temp=INT_MAX;
                if(temp!=m) return false;
                }
        }
        return true;
    }
};

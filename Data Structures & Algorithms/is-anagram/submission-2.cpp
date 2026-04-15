class Solution {
public:
    bool isAnagram(string s, string t) {
        int n = s.length();
        int m = t.length();
        if(n != m){
            return false;
        }
        vector<char> sc(s.begin(), s.end());
        vector<char> tc(t.begin(), t.end());
        sort(sc.begin(), sc.end());
        sort(tc.begin(), tc.end());
        for(int i = 0; i < n; i++){
            if (sc[i] != tc[i]){
                return false;
            }
        }
        return true;

    }
};

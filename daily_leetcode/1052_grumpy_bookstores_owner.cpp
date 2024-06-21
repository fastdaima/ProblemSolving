#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
using namespace std;

class Solution {
public:
    int maxSatisfied(vector<int>& c, vector<int>& g, int m) {
        int us = 0;
        int n = c.size();

        for(int i=0; i<m; ++i){
            // cout << i;
            us += c[i]*g[i];
        }
        int max_us = us; 

        for(int i=m;i<n;++i){
            us += c[i]*g[i];
            us -= c[i-m]*g[i-m];
            max_us =( us > max_us) ? us : max_us; 
        }

        for(int i=0;i<n;++i){
            max_us += c[i]*(1-g[i]);
        }

        return max_us;
    }

};

int main() {
    vector<int> customers = {1,0,1,2,1,1,7,5};
    vector<int> grumpy =    {0,1,0,1,0,1,0,1};
                            // 1 1 1 7 = 10 
                            // 

    int minutes = 3;

    Solution s;

    cout << s.maxSatisfied(customers, grumpy, minutes);

}
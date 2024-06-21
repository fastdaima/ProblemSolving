#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath> 

using namespace std; 

class Solution {
public:
    bool can_place_balls(int x, vector<int>& position, int m) {
        int balls_placed = 1; 
        int current_pos = 0;

        int prev_pos = position[0];

        for(int ind=1; ind<position.size() && balls_placed<m; ++ind) {
            current_pos = position[ind];
            if (current_pos - prev_pos >= x ) {
                balls_placed++;
                prev_pos = current_pos;
            }
        }

        return balls_placed==m;
    }
    
    
    int maxDistance(vector<int>& position, int m) {
        int answer = 0;
        int n = position.size();
        sort(position.begin(), position.end());

        int low =1 ;
        int high = ceil(position[n-1]/(m-1.0));

        // cout<< "high value" << high << '\n';

        while (low<=high) {
            int mid = low+(high-low)/2;
            if (can_place_balls(mid, position, m)) {
                answer = mid; 
                low = mid+1;
            } else {
                high = mid-1;
            }
        }
        return answer;
    }
};


int main() {
    Solution s;

    vector<int> position = {1,2,3,4,7};
    int m = 3;
    cout << s.maxDistance(position, m) << '\n';
    return 1;
}
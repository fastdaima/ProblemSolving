// https://leetcode.com/problems/coin-change/


#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;


bool compare(int a, int b) {
    return a<=b;
}


int coinChange(vector<int>& coins, int amount) {
    int out = 0;
    sort(coins.begin(),coins.end());
    vector<int>::iterator lb;
    int n = coins.size();
    while ( amount > 0) {
            
        lb = lower_bound(coins.begin(), coins.end(), amount, compare);

        int m = coins[lb-coins.begin()-1];
        amount -= m;
        out++;
    }

    if (out == 0) {
        return -1;
    } else {
        return out;
    }
    return 0;
        
}

int main() {
    vector<int> inp = {1,2,5,10,20,50,100,200,500,2000};

    int n = 225;

    cout << coinChange(inp,n);

   
    return 0;
}

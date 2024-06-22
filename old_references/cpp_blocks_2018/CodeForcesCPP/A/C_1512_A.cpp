// https://codeforces.com/contest/1512/problem/A
#include<iostream>
#include<algorithm>
#include <sstream>
#include <vector>

using namespace std;

#define int             long long
#define pb              push_back
#define mp              make_pair

void read_input_write_output()
{
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#ifndef ONLINE_JUDGE
    freopen("D:\\91790\\CodeForces\\Testing\\input.txt", "r", stdin);
    freopen("D:\\91790\\CodeForces\\Testing\\output.txt", "w", stdout);
#endif
}



int32_t main()
{
    read_input_write_output();
    int t,t2,n,val;cin>>t;
    vector<pair<int,int>> inp;
    int count = 0;

    while(t--) {
        cin>>n;
        t2 =n;
        count = 0;
        while(n--) {
            cin>>val;
            count++;
            inp.push_back(make_pair(val,count));

        }
        vector<pair<int,int>> temp(inp);
        sort(temp.begin(), temp.end());
      

        int key = (temp[0].first!=temp[1].first) ? temp[0].second:temp[t2-1].second;
        cout << key << '\n';
        inp.clear();
        temp.clear();
    }

    return 0;
}

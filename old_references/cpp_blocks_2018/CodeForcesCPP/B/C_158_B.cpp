// https://codeforces.com/contest/158/problem/B
#include<iostream>
#include<vector>
#include<algorithm>

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
    int t,val,taxi_count=0; cin>>t;
    int inp[5] = {0};


    while (t--) {
        cin >> val;
        inp[val] ++;
    }

    while (inp[1]!=0 && inp[3]!=0) {
        taxi_count++;
        inp[1]--;inp[3]--;
    }

    while (inp[2]>1) {
        taxi_count++;
        inp[2]-=2;
    }

    while (inp[2]==1 && inp[1]>0) {

        if(inp[1]/2 >= 1) {
            taxi_count++;
            inp[2]--;
            inp[1] -= 2;
        } else {
            taxi_count++;
            inp[2]--;
            inp[1]--;
        }
    }

    if (inp[1]>4) {
        taxi_count += inp[1]/4;
        inp[1] = inp[1]%4;
    }

    if (inp[1]!=0) {
        inp[1] =1;
    }


    cout << taxi_count + inp[4] + inp[2] + inp[3] + inp[1] << '\n';

    return 0;
}
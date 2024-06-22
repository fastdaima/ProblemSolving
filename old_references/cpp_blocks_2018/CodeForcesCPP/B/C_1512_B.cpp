// https://codeforces.com/contest/1512/problem/B
#include<iostream>
#include<algorithm>
#include <string>
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
    int t,n;
    cin>>t;
    string val,temp;
    vector<pair<int,int>> index;
    int x3,x4,y3,y4;
    while(t--) {
        cin>>n;
        vector<vector<string>> inp;
        inp.resize(n);
        for (int i=0;i<n;i++) {
            inp[i].resize(n);
            cin>> val;
            for (int j=0;j<val.size();j++) {
                temp = val[j];
                if (temp == "*") {
                    index.push_back(make_pair(i,j));
                }
                inp[i][j]=temp;
            }

        }



        if (index[0].first == index[1].first) {
            if(index[0].first +1 < n) {
                x3 = index[0].first +1;
                x4 = index[1].first +1;
                y3 = index[0].second;
                y4 = index[1].second;
            } else {
                x3 = index[0].first -1;
                x4 = index[1].first -1;
                y3 = index[0].second;
                y4 = index[1].second;
            }
        }

        else if (index[0].second == index[1].second) {
            if(index[0].second +1 < n) {
                y3 = index[0].second +1;
                y4 = index[1].second +1;
                x3 = index[0].first;
                x4 = index[1].first;
            } else {
                y3 = index[0].second -1;
                y4 = index[1].second -1;
                x3 = index[0].first;
                x4 = index[1].first;
            }
        }

        else {

            x3 = index[0].first;
            y3 = index[1].second;

            x4 = index[1].first;
            y4 = index[0].second;
        }

        inp[x3][y3] = "*";
        inp[x4][y4] = "*";

        for (int i=0;i<n;i++) {
            for (int j=0;j<n;j++) {
                cout << inp[i][j];
            }
            cout<< '\n';
        }

        inp.clear();
        index.clear();
    }

    return 0;
}

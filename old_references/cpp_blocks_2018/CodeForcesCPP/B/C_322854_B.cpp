#include<iostream>
#include<vector>
#include<math.h>
#include<algorithm>
using namespace std;


#define ff              first
#define ss              second
#define int             long long
#define pb              push_back
#define mp              make_pair
#define pii             pair<int,int>
#define vi              vector<int>
#define mii             map<int,int>

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
    int t; cin>>t;
    int val;
    int left=0,right=0;

    vector<int> input_;
    vector<int> output_;

    for(int i=0; i<t;i++) {
        cin >> val;
        input_.pb(val);
    }

    for (int i=0;i<t;i++) {
        output_.pb(i+1);
    }




    for(int i=0;i<input_.size();i++) {
        if (input_[i]!=i+1) {
            left = i;
            break;
        }
    }




    for(int i=input_.size()-1;i>-1;i--) {
        if (input_[i]!=i+1) {
            right = i;
            break;
        }
    }

    if (right==0 && left==0) {
        cout << "0 0\n";
    }
    else
    {
        reverse(input_.begin()+left,input_.begin()+right+1);
        if (input_ == output_) {
          cout << left+1 << " " << right+1 << '\n';
        } else {
          cout << "0 0\n";
        }

    }

    return 0;
}
#include<iostream>
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
    int n,k; cin>>n>>k;
    if(2*n-1<k)
        cout << "0\n";
    else if (k<=n) {
       int val = (k%2 == 0) ? k/2-1:k/2;
       cout << val << '\n';
    } else if ( k>n ) {
        int max_ = n;
        int min_ = max(n,k)-min(n,k);
        cout << (max_ -min_ + 1)/2 << '\n';
    }
    return 0;
}
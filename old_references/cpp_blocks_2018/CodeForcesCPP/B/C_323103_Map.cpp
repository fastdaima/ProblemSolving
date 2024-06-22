
// https://codeforces.com/gym/323103/problem/A
#include<iostream>
#include<algorithm>
#include<map>

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
    map<int,int> m;

    read_input_write_output();
    int n,k; cin>>n>>k;
    int left=1,right=n,count=0;
    if (n+n-1<k) {
        cout << "0\n";
        return 0;
    }

    for (int i=1;i<n+1;i++)
        m[i]++;

    for (int i=1;i<n+1;i++) {
        count += m[k-i];

        // same pair not supported (i.2) (i,i)
        if (k-i==i) {
            count--;
        }
    }

    cout << count/2 << '\n';
    return 0;
}
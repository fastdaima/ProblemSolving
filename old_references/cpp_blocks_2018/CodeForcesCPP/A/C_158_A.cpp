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
    int n,k;
    cin >> n >> k;

    vector<int> arr;
    int count=0, val;
    for(int i=0;i<n;i++) {
        cin >> val;
        arr.push_back(val);
    }

    val = arr[k-1];

    for(int i=0;i<n;i++) {
        if(arr[i] >= val && arr[i] > 0) {
            count ++;
        } else {
            break;
        }

    }


    cout << count << '\n';
    return 0;
}
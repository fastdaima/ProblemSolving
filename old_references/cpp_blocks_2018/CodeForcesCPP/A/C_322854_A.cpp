#include<iostream>
#include<string>
#include<algorithm>
#include<math.h>

using namespace std;

void read_input_write_output()
{
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#ifndef ONLINE_JUDGE
    freopen("D:\\91790\\CodeForces\\Testing\\input.txt", "r", stdin);
    freopen("D:\\91790\\CodeForces\\Testing\\output.txt", "w", stdout);
#endif
}

int main()
{
    read_input_write_output();
    long long int t; cin>>t;
    string out="YES";
    long long int w,h;
    cin >> w >> h;
    long long int prev = max(w,h),curr_max, curr_min=0;
    t-=1;
    while (t--) {
        cin >> w >> h;
        curr_min = min(w,h);
        curr_max = max(w,h);
        if (curr_max <= prev) {
            prev = curr_max;
        }
        else if (curr_min<=prev) {
            prev = curr_min;
        }
        else {
            out = "NO";
            break;
        }

    }
    cout << out << '\n';
    return 0;
}
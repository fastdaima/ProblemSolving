#include<iostream>
#include<set>
#include<string>
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

    char a[100];
    int t; cin>>t;
    while (t--) {
        int n,w,val,box_height,remaining_width;

        cin >> n >> w;

        multiset<int> all_weights;

        while(n--) {
            cin >> val;
            all_weights.insert(val);
        }

        box_height = 1;
        remaining_width = w;

        while(!all_weights.empty()) {
            auto it = all_weights.upper_bound(remaining_width);

            if (it!=all_weights.begin()) {
                it--;
                val = *it;
                remaining_width -= val;
                all_weights.erase(it);
            }
            else {
                box_height ++;
                remaining_width = w;
            }
        }
        cout << box_height << '\n';
    }


    return 0;
}

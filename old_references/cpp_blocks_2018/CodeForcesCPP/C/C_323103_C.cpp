
//https://codeforces.com/gym/323103/problem/C

#include<iostream>
#include<map>
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
int arr[200004];
int32_t main()
{
    read_input_write_output();
    int n;cin >> n;
    int val;

    vector<int> unique_numbers;
    vector<int> dup_numbers(n+1,0);
    map<int,int> perm;
    vector<int> v;
    int change_count=0,unique_ptr=0;



    for(int ind=0;ind<n;ind++) {
        cin >> val;
        v.pb(val);
        arr[val]++;
    }

    for(int ind=1;ind<n+1;ind++) {
      if (arr[ind]==0) unique_numbers.pb(ind);
    }



    for(int ind=0;ind<n;ind++) {
        if(arr[v[ind]]>1) {
            if (v[ind]<unique_numbers[unique_ptr] && dup_numbers[v[ind]]==0) {
                dup_numbers[v[ind]] =1;
                continue;
            }
            arr[v[ind]]--;
            v[ind] = unique_numbers[unique_ptr];
            unique_ptr++;
            change_count++;
        }
    }

    cout<<change_count<<'\n';
    for(auto vi:v) {
        cout<<vi << " ";
    } cout << '\n';

    return 0;
}
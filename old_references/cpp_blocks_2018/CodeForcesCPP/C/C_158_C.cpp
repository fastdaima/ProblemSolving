// https://codeforces.com/contest/158/problem/C

#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<cstring>

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
    string slash("/");
    string input,input2,temp;
    vector<string> output;
    output.push_back("/");
    read_input_write_output();

    int t; cin>>t;

    while (t--) {
        cin >> input;

        if (strstr(input.c_str(),"pwd")) {
            if (output[output.size() - 1] != "/") {
                output.push_back("/");
            }
            for(auto v:output) {
                cout<<v;
            }
            cout<<'\n';
        } else if (strstr(input.c_str(),"cd")) {
            cin>> input2;
            input2 += '/';
            temp ="";
            for (int i=0;i<input2.size();i++) {
                if (input2[i]=='/') {
                    if (i==0) {
                        if (output.size()>0) {
                            output.erase(output.begin(), output.end());
                        }
                    }

                    if (temp.size() != 0) {
                         if (output.size() ==0 || output[output.size() - 1] != "/") {
                             output.push_back("/");
                         }
                         if (temp == "..") {
                             output.pop_back();
                             output.pop_back();
                             temp ="";
                         } else {
                             output.push_back(temp);
                             temp = "";
                         }
                    }
                } else {
                    temp += input2[i];
                }
            }
        }
    }
    return 0;
}
#include<iostream>
#include <string>
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
    string s;
    //read_input_write_output();
    while (getline(cin,s)) {
        cout << "NO\n";
        fflush(stdout);
    }
    return 0;
}
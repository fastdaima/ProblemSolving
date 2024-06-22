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

void permute(char a[], int i, set<string> &s) {
    if (a[i]=='\0') {
        string t(a);

        s.insert(t);
        return;
    }

    for (int j=i; a[j] !='\0'; j++) {
        swap(a[i],a[j]);
        permute(a, i+1,s);
        swap(a[i],a[j]);
    }
}

int main()
{
    read_input_write_output();

    char a[100];
    int t; cin>>t;
    while (t--) {
        cin >> a;
        set<string> s;
        permute(a, 0, s);

        for (set<string>::iterator it = s.begin(); it != s.end(); it++) {
            cout << *it << " ";
        }

        cout << '\n' << s.size() << '\n';
    }
    return 0;
}
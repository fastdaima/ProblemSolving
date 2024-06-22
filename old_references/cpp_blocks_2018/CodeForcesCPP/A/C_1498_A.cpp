// https://codeforces.com/contest/1498/problem/A

#include <iostream>
#include <string>
using namespace std;
typedef long long ll;

ll find_digits(ll a) {
    ll sum =0;
    string D = std::to_string(a);
    for (int i=0;i<D.size();i++) {
        sum  += D[i] - '0';
    }
    return sum;
}

ll gcd(ll a, ll b) {
    if (b==0) {
        return a;
    }
    return gcd(b,a%b);
}

int main() {
    int t;

    cin >>t;

    while(t--) {
        ll a;
        cin >> a;
        ll b = find_digits(a);
        ll val = gcd(a,b) ;

        if (val > 1) {
            cout << a << '\n';
        } else {
            while (val < 2) {
                a += 1;
                b = find_digits(a);
                val = gcd(a, b);
            }
            cout << a << '\n';
        }
    }
    return 0;
}
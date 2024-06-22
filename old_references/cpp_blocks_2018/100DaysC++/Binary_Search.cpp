#include<iostream>
#include<algorithm>

using namespace std;


int main() {
    int a[] = {12,56,745,343};
    int n = sizeof(a)/sizeof(int);
    int key = 56;

    auto present = binary_search(a,a+n,key);    
    
    if (present ) {
        auto it = lower_bound(a,a+n,key);

        auto it2 = upper_bound(a,a+n,key);

        cout << *it << " " << it-a << " " <<a[it-a];

        cout << '\n' << *it2 << " " << it2-a << " " <<a[it2-a];

        cout <<"\nFrequency of key 56 " << it2-it; 

    }
    return 0;
}
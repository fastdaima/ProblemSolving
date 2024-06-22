#include<iostream>
#include<algorithm>

using namespace std;


int main() {
    int a[] = {12,56,745,343};
    int n = sizeof(a)/sizeof(int);
    int key = 56;

    auto it = find(a,a+n,key);    
    cout << it - a << " " << *it << " " << a[it-a];
    return 0;
}
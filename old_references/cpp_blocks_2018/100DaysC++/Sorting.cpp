#include<iostream>
#include<algorithm>

using namespace std;



bool compare(int a, int b) {
    return a > b;
}

int main() {
    int a[] = {12,56,745,343};
    int n = sizeof(a)/sizeof(int);

    // ascending order
    sort(a,a+n);

    for(auto b:a) {
        cout << b << " ";
    }

    cout << '\n';

    // descending order 
    sort(a,a+n,compare);

    for(auto b:a) {
        cout << b << " ";
    }


    return 0;
}
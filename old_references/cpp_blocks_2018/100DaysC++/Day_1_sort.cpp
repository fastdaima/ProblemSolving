#include <iostream>
#include <algorithm>
using namespace std;

bool myCompare(int a, int b) {
    return a>b;
}


int main() {
    int a[] = {9,10,3,45,98};

    int n = sizeof(a)/sizeof(int);

    cout << "ascending order \n";
    sort(a,a+n);

    for(int i=0;i<n;i++) {
        cout << *(a+i) << " ";
    }
    cout << '\n';

    cout << "descending order \n";

    sort(a,a+n,myCompare);
    for(int i=0;i<n;i++) {
        cout << *(a+i) << " ";
    }
    cout << '\n';


    return 0;
}


// output

// ascending order
// 3 9 10 45 98
// descending order
// 98 45 10 9 3


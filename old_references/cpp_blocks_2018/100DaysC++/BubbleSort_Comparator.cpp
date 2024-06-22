#include<iostream>
using namespace std;

bool compare(int a, int b) {
    return a<b;
}

void bubble_sort(int a[],int n, bool (&cmp)(int a, int b)) {

    for(int i=0;i<n;i++) {
        for (int j=i+1;j<n;j++ ) {
            if(cmp(a[i],a[j])) {
                swap(a[i],a[j]);
            }
        }
    }

}

int main() {
    int a[] = {12,56,745,343};
    int n = sizeof(a)/sizeof(int);
    int key = 56;

    bubble_sort(a,n,compare);

    for(auto b:a) {
        cout << b << " ";
    }

    return 0;
}
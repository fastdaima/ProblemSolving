#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;


int main() {
    vector<int> inp = {1,2,5,10,20,50,100,200,500,2000};
    int n = sizeof(inp)/sizeof(int);
    
    swap(inp[0],inp[4]);
    
    for(auto v:inp) {
        cout << v << " "; 
    }

    cout << '\n' << min( 345,67);
    cout << '\n' << max(67,345);

    cout << '\n';
    next_permutation(inp.begin(),inp.end());

    int arr[] = {1,2,3 ,4,5};

    reverse(arr,arr+2);
    for(auto v:arr) 
        cout << v << " ";
    
    cout << "\n";

    for(auto v:inp)
        cout << v << " "; 
    
    cout << "\n";

    next_permutation(inp.begin(),inp.end());
    for(auto v:inp)
        cout << v << " "; 

    return 0;
}

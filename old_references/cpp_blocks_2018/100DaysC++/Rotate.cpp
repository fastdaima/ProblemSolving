#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;


int main() {
    vector<int> inp = {1,2,5,10,20,50,100,200,500,2000};
    int n = sizeof(inp)/sizeof(int);
    rotate(inp.begin(),inp.begin()+3,inp.end());

    for(auto v:inp) {
        cout << v << " "; 
    }

    cout << '\n';
    next_permutation(inp.begin(),inp.end());

    for(auto v:inp)
        cout << v << " "; 


    return 0;
}

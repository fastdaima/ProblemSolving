#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;


int main() {

    pair<string,int> p;
    p.first = "a";
    p.second = 1;

    cout << p.first << " " << p.second << '\n';

    // another way 
    // supports(pairs) and vector(pairs)

    pair<string,int> p2(p);

    cout << p2.first << " " << p2.second << '\n';
    
    pair<string,int> p3 = make_pair("df",3);

    cout << p3.first << " " << p3.second << '\n';

    pair< pair<string,int>,  int> bwc;

    bwc.first.first = "Rank";
    bwc.first.second = 1;

    bwc.second = 100000;

    cout << bwc.first.first << " " << bwc.first.second << " " << bwc.second << '\n';
 

    return 0;
}

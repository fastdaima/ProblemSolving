#include <iostream>
using namespace std;


#include <set>

int main() {
    set<int> s;
    int arr[] = {10,122,11,233,25,1,1,2,3};
    int size  = sizeof(arr)/sizeof(int);
    for (int i=0; i<size; i++) {
        // insertion
        s.insert(arr[i]);
    }
    for (set<int>::iterator it=s.begin();it!=s.end();it++) {
        cout << *it << " ";
    }
    cout << '\n';

    // erase
    s.erase(122);

    // find the iterator of the element to be deleted
    auto it = s.find(2);
    s.erase(it);

    for (set<int>::iterator it=s.begin();it!=s.end();it++) {
        cout << *it << " ";
    }


    // Implementing dictionary
    set<pair<int,int>> dict ;

    dict.insert(make_pair(10,20));
    dict.insert(make_pair(10,30));
    dict.insert(make_pair(20,30));
    dict.insert(make_pair(20,40));
    dict.insert(make_pair(30,30));
    dict.insert(make_pair(40,10));
    dict.insert(make_pair(50,80));
    dict.insert(make_pair(45,90));
    dict.insert(make_pair(20,50));

    cout << "\nBefore insertion / deletion\n";


    for (auto ptr:dict){
        cout << "key " << ptr.first << " value " << ptr.second << '\n';
    }


    dict.erase(dict.find(make_pair(10,30)));

    dict.insert(make_pair(10,40));

    cout << "\nAfter inser  tion / deletion\n";
    for (auto ptr:dict){
        cout << "key " << ptr.first << " value " << ptr.second << '\n';
    }


    return 0;
}
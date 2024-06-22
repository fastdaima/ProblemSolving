#include <iostream>
#include<unordered_map>
#include<string>
using namespace std;


// map used as balanced tree red black tree
// unordered map used as hash table 


// supported operations

// find()
// rehash()
// insert()
// erase()
// count()
// load_factor() load_factor  = current_size / bucket_count
// clear()
// begin()
// end()
// operator[]


// template <class T>

// Comparator template
template <class T, class Compare>
int search(T arr[],int n, T elementToSearch, Compare obj) {
    for (int pos=0;pos<n;pos++) {
        if (obj(arr[pos],elementToSearch)==true) {
            return pos;
        }
    }
};

// Iterator template
template <class ForwardIterator, class T, class Compare>
ForwardIterator search(ForwardIterator beginO, ForwardIterator endO, T elementToSearch, Compare obj)
{
    while(beginO!=endO){
        if(obj((*beginO),elementToSearch)==true) {
            break;
        }
        ++beginO;
    }
    return beginO;
}

int main() {
    unordered_map<string,int> h;

    // initialize
    h["apple"]=10;
    h["apple"]=100;

    // check element exist
    if (h.count("apple")!=0) {
        cout << h["apple"] << '\n';
    }

    // insertion
    h.insert(make_pair("mango",99));


    cout << "enter fruit name\n";
    string f;
    cin>>f;

    if (h.count(f)) {
        cout << h[f];
    } else {
        cout << "fruit illai\n";
    }

    // print unordered_map 
    // here auto p is pair<string, int>
    for (auto p:h) {
        cout << p.first << "  " << p.second  << '\n';
    }

    // delete a fruit
    h.erase("mango");

    for (auto p:h) {
        cout << p.first << "  " << p.second  << '\n';
    }
    return 0;
}
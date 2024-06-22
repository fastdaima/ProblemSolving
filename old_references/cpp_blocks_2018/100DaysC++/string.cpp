// wraps char* array in string

#include<string>
#include<iostream>

using namespace std;

void print(string o) {
    cout << o << "\n";
}

int main() {
    string on;

    print (on);

    string off("cppblocks");

    print (off);

    off += " I love c++ and python ";

    print (off);

    string neutral(off);

    neutral += "and mastery";
    print (to_string(neutral.length()));
    int n = neutral > off;
    cout <<  n<< "\n";

    print(to_string(off.length()));

    // clearning the string
    off.clear();

    print(to_string(off.length()));

    cout << neutral[0];
    cout << "\n";
    
    // finding word position
    size_t index = neutral.find("c++");

    cout << index << "\n";

    neutral.erase(index,5);

    print(neutral);

    // three ways to loop out an string 
    // 1 for loop
    for(int i=0;i<neutral.length();i++) {
        cout << neutral[i]<< " ";
    }
    cout << '\n';
    // 2 iterator

    for(auto it=neutral.begin();it!=neutral.end();it++) {
        cout << *it << " ";
    }
    cout << '\n';

    // 3 foreach loop

    for(auto v:neutral) {
        cout << v << " ";
    }
    return 0;
}
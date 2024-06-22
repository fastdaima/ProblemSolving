#include<iostream>
#include<string>
#include<algorithm>

using namespace std;

// user defined function to sort based on string length
bool compare(string a, string b) {
    if (a.length() == b.length()) {
        // if a and b length are equal compare based on alphabetical order
        return a < b;
    }
    // else returns based on length
    return a.length() < b.length();

    // if your sorting condiions are 
    // 1. if string length equal compare on lexicographical order
    // 2. or else return elements which have biggest length
    // use a.length() > b.length()
}

int main() {

    int n;
    cin >> n;

    // one
    // this way of getting input works for inputs greater than one word
    // cin.get()
    // getline(cin,s[i])

    // two
    // cin >> string 
    // string_array[index] = string will only work for single word inputs

    cin.get();
    string s[100];
    string a;
    for(int i=0;i<n;i++) {
        getline(cin,s[i]);
    }

    // sorting function from algorithm.h
    sort(s,s+n,compare);

    for(int i=0;i<n;i++) {
        cout << s[i] << '\n';
    }

    return 0;
}
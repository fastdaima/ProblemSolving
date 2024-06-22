
// Input :
//     - n : total number of strings 
//     - followed by n number of strings containing digits and spaces
//         - constant number of spaces in n strings i.e) if string in first line contains 2 spaces all the remaining n-1 strings will contain 2 spaces.
//         - spaces are used for splitting strings to columns 
//         - for ex :
//             - Input : 2
//                       abc def ghi
//                       jkl lmn nop

//                     str : 0    1   2
//                         0 abc def ghi 
//                         1 jkl lmn nop
            
//     - key : column number denoting based on which column in strings the sorting should be done
//     - reversed : boolean value denoting whether we should reverse the array or not after sorting
//     - comparison-type : 
//         - lexicographic: sorting based on comparing elements at each index
//             - for ex: lexicographical comparing of 2 strings
//                 - Input : 2
//                           string1 = "139"
//                           string2 = "14"
//                           - At index = 0:
//                             - both values are same 1==1 => continue
//                           - At index = 1:
//                             - string1[1] < string2[1] :
//                                 - so the result will be returned as string2>string1
//         - numeric: comparing strings by their numerical values

// Output: 
//     - printing the strings line by line after sorting and reordering                       

// blog link : https://daywithalgorithm.xyz/2021/05/14/sort-the-strings/
#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;

#define int             long long
#define pb              push_back
#define mp              make_pair


void read_input_write_output()
{
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#ifndef ONLINE_JUDGE
    freopen("D:\\91790\\CodeForces\\Testing\\input.txt", "r", stdin);
    freopen("D:\\91790\\CodeForces\\Testing\\output.txt", "w", stdout);
#endif
}

// getting key from string based on index
string get_key(string basicString, int key) {
    char* s = strtok((char *)basicString.c_str()," ");
    while (key>1) {
        s = strtok(NULL," ");
        key--;
    }
    return std::string(s);
}
// converting string to int

int string_to_int(string a) {
    int prod = 1,sum=0;

    for(int i=a.size()-1;i>-1;i--) {
        int cur = (a[i]-'0')*prod;
        sum += cur;
        prod *=10 ;
    }
    return sum;
}

// compare function for numerical type
bool numericCompare(const pair<string,string> &p1, const pair<string,string> &p2) {
    int a = string_to_int(p1.second);
    int b = string_to_int(p2.second);
    return a <b;
}

// compare function for lexicographical type
bool lexicoCompare(const pair<string,string> &p1, const pair<string,string> &p2) {
    return p1.second < p2.second;
}




int32_t main()
{
    read_input_write_output();
    int n, key;
    string reversal, sorting_type;
    cin>>n;
    cin.get();

    vector<string> string_arr(n);

    for(int i=0;i<n;i++) {
        getline(cin,string_arr[i]);
    }

    cin>>key>>reversal>>sorting_type;

    vector<pair<string,string>> array_key_pair;

    for(int i=0;i<n;i++) {
        array_key_pair.push_back(make_pair(string_arr[i],get_key(string_arr[i],key)));
    }

    if (sorting_type=="numeric") {
        sort(array_key_pair.begin(),array_key_pair.end(),numericCompare);
    } else {
        sort(array_key_pair.begin(),array_key_pair.end(),lexicoCompare);
    }

    // reversing the string

    if (reversal=="true") {
        for(int i=0;i<n/2;i++) {
            swap(array_key_pair[i],array_key_pair[n-1-i]);
        }
    }



    for(int i=0;i<n;i++) {
        cout << array_key_pair[i].first << '\n';
    }


    return 0;
}



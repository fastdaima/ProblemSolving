#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;

char* my_strtok(char *input_string, char delimeter) {
    // declared as static to remember the next word starting position or else
    // same word will be returned as output
    static char * input = NULL;

    if(input_string!=NULL) {
        input = input_string;
    }

    // executed at final iteration
    if(input==NULL) {
        return NULL;
    }

    int i = 0;
    
    // declaring output size based on total input size
    char* output = new char[strlen(input)+1];

    for(;input[i]!='\0';i++) {
        if(input[i]!=delimeter) {
            output[i] = input[i];
        } else {
            output[i] = '\0';
            // assigns input starting positon to the next word
            input = input + i + 1;
            return output;
        } 
    }

    // since there is no delimiter at the end
    if(input[i]=='\0') {
        output[i] = '\0';
        input = NULL;
    }
    return output;

}


int main() {
    char x[100] = "I am practising 30 pomodoros daily on programming";

    // inbuilt string tokenizer function
    char *ptr= strtok(x," ");

    while (ptr!=NULL) {
        cout << ptr <<'\n';
        ptr = strtok(NULL," ");
    }

    // custom string tokenizer

    char y[100] = "I am practising 30 pomodoros daily on programming";

    char * ptr2 = my_strtok(y,' ');
    int count = 0;
    while(ptr2!=NULL) {
        count ++;
        cout << ptr2 << "\n";
        ptr2 = my_strtok(NULL,' ');
    }
    
    return 0;
}
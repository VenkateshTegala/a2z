#include<bits/stdc++.h>
using namespace std;

int main() {
    int arr[5];


    //2d array
    int arr_2[3][5];
    arr_2[1][3] = 3;
    cout << arr_2[0][4];

    //using string as array
    string s = "venkycena";
    int len = s.size();
    s[len - 1] = 'z';
    cout << s;
    cout << s[len - 1];

    return 0;
}
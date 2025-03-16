#include<iostream>
using namespace std;
int main() {
    //switch for week
    int day;
    cout << "Enter a day in num : ";
    cin >> day;
    switch (day)
    {
    case 1:
        cout << "Sunday";
        break;
    case 2:
        cout << "Monday";
        break;
    case 3:
        cout << "Wednesday";
        break;
    case 4:
        cout << "Thursday";
        break;
    case 5:
        cout << "Friday";
        break;
    case 6:
        cout << "Saturday";
        break;
    default:
    cout << "Invalid";
        break;
    }
}
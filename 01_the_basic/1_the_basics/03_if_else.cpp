#include<iostream>
using namespace std;
int main() {
    int age;
    cout << "Enter your age : ";
    cin >> age;
    if(age < 18) {
        cout << "You are not an adult";
    } else {
        cout << "You are an adult";
    }

    cout << "\n";
    //A school has the following rules:
    int marks;
    cout << "Enter your marks: ";
    cin >> marks;
    if(marks < 25) {
        cout << "F";
    } else if (marks >= 25 && marks <= 30) {
        cout << "E";
    } else {
        cout << "A";
    }
    return 0;
}
#include<iostream>
using namespace std;

void printName() {
    //void function
    cout << "Hi Venky\n";
}

void printNamewith(string name) {
    cout << "Hi " << name << "\n";
}

int sum(int a, int b) {
    return a + b;
}

int main() {
    //void
    //return 
    //parameterized
    //non parameterized

    printName();
    printNamewith("Cena");
    int sum_value = sum(5, 3);
    cout << "Sum of two numbers : " << sum_value << "\n";
    return 0;
}


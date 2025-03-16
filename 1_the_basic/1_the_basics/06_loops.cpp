#include<iostream>
using namespace std;
int main() {
    // using for loop
    int i;
    for (i = 1; i <= 5; i++) {
        cout << "Venky Cena\n";
    }
    cout << i;

    //while loop
    cout << "\nWhile loop\n";
    int y = 5;
    while(y >= 0) {
        cout << "Venky Cena\n";
        y--;
    }

    //do while
    int z = 0;
    do {
        cout << "Value of z :" << z;
    }while (z > 0);
    

    return 0;
}
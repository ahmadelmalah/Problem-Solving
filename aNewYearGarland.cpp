using namespace std;
#include <iostream>

int main() {
    int numOfLines;
    cin >> numOfLines;
    for(int i=0; i<numOfLines; i++) {
        int num1;
        int num2;
        int num3;
        cin >> num1;
        cin >> num2;
        cin >> num3;
        if (num1>(num2+num3+1) || num2>(num1+num3+1) || num3>(num1+num2+1)) {
            cout << "No" << endl;
        } else {
            cout << "Yes" << endl;
        }
    }
    return 0;
}
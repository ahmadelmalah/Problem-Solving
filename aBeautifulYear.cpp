using namespace std;
#include <iostream>
#include <string>

bool isDistinct(int year) {
    string year_s = to_string(year);
    return (year_s[0] != year_s[1] && year_s[0] != year_s[2] && year_s[0] != year_s[3] && year_s[1] != year_s[2] && year_s[1] != year_s[3] && year_s[2] != year_s[3]);
}

int main() {
    int input;
    int year;
    cin >> input;
    year = input;
    do {
        year++;
    } while (!isDistinct(year));
    
    cout << year << endl;
    return 0;
}


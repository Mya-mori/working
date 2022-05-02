#include <iostream>
using namespace std;

int main() {
    cout << "Start Game" << endl;

    // 年齢の区間
    int left = 20;
    int right = 36;

    // 年齢推測
    while(right - left > 1 ) {
        int mid = left + (right - left) / 2;

        // midより年齢を推測
        cout << "Is The Age Less Than " << mid << "?(yes/no)" << endl;
        string ans;
        cin >> ans;

        if (ans == "yes") {
            right = mid;
        }
        else {
            left = mid;
        }
    }

    // 年齢を出力
    cout << "Your Age Is " << left << "!" << endl;
}
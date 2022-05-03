#include <iostream>
#include <vector>
using namespace std;

const vector<int> value = {500, 100, 50, 10, 5, 1};

int main() {
    int X;
    vector<int> a(value.size());
    cin >> X;
    for (int i = 0; i < value.size(); i++) {
        cin >> a[i];
    }

    int result = 0;
    for (int i = 0; i < value.size(); i++) {
        int add = X/value[i];

        if (add > a[i]) {
            add = a[i];
        }

        X -= add * value[i];
        result += add;
    }
    cout << result << endl;
}
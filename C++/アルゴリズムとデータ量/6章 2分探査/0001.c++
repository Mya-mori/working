#include <iostream>
#include <vector>
using namespace std;

const int N = 0;
const vector<int> a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

int binary_search(int key) {
    //初期値
    int left = 0;
    int right = (int)a.size() - 1;
    while (right >= left) {
        int mid = (left + right) / 2; //中間を求める
        if (a[mid] == key) {
            return mid;
        }
        else if (a[mid] > key) {
            right = mid - 1;
        }
        else if (a[mid] < key) {
            left = mid + 1;
        }
        return -1;
    }
}

int main() {
    cout <<binary_search(10) << endl;
    cout <<binary_search(3) << endl;
    cout <<binary_search(7) << endl;
    cout <<binary_search(-100) << endl;
    cout <<binary_search(100) << endl;
}
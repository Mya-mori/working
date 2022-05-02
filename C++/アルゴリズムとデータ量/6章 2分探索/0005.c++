#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
const long long INF = 20000000000;

int main() {
    //入力
    int N;
    cin >> N;
    vector<int> h(N), a(N);
    for (int i = 0; i < N; i++) {
        cin >> h[i];
    }

    long long left = 0;
    long long right = INF;
    while (right - left > 1) {
        long long mid = (left + right) / 2;

        //判定
        bool ok = true;
        vector<long long> t(N, 0);

        for (int i = 0; i < N; i++) {
            if (mid < h[i]) {
                ok = false;
            }
            else {
                t[i] = mid - h[i];
            }

            sort(t.begin(), t.end());
            for (int i = 0; i < N; i++) {
                if (t[i] < a[i]) {
                    ok = false;
                }
            }

            if (ok) {
                right = mid;
            }
            else {
                left = mid;
            }
        }
    cout << right << endl;
}


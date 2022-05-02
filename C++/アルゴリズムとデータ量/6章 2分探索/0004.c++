#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
const int INF = 20000000000;

int main() {
    //入力
    int N, K;
    cin >> N >> K;
    vector<int> a(N), b(N);
    for (int i = 0; i < N; i++) {
        cin >> a[i];
    }
    for (int i = 0; i < N; i++) {
        cin >> b[i];
    }

    //暫定値
    int min_value = INF;

    //bをソート
    sort(b.begin(), b.end());

    //aを固定して解く
    for (int i = 0; i < N; i++) {
        // bの中でK - a[i]以上で最小値を示す
        auto iter = lower_bound(b.begin(), b.end(), K - a[i]);

        int val = *iter;

        //min_valueと比較
        if (a[i] + val < min_value) {
            min_value = a[i] + val;
        }
    }
    cout << min_value << endl;
}
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
    
}
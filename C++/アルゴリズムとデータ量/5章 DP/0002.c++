#include <iostream>
#include <vector>
using namespace std;

template<class T> void chmin(T& a, T b) {//&参照型 Tをaとして返す
    if (a < b){
        a = b;
    }
}
const long long INF = 1LL << 60;

int main() {
    //入力
    int N;
    cin >> N;
    vector<int> h(N);
    for (int i = 0; i < N; i++){
        cin >> h[i];
    }

    //初期化
    vector<long long> dp(N, INF);

    //ループ
    for (int i = 1; i < N; i++){
        chmin(dp[i], dp[i - 1] + abs(h[i] - h[i - 1]));
        if (i > 1){
            chmin(dp[i], dp[i - 2] + abs(h[i] - h[i - 2]));
        }
    }

    cout << dp[N - 1] << endl;
}